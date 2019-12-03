class WireGrid:
    def __init__(self):
        self.wire_grid = {}

    def add_wire(self, wire_name: str):
        self.wire_grid[wire_name] = {
                                    "current_position": [0, 0],
                                    "path_positions": []
                                    }

    def get_current_position(self, wire_name: str):
        return self.wire_grid[wire_name]["current_position"]

    def set_current_position(self, wire_name: str, position: list):
        self.wire_grid[wire_name]["current_position"] = position

    def add_path_position(self, wire_name: str, position: tuple):
        self.wire_grid[wire_name]["path_positions"].append(position)

    def move(self, direction: str, count: int, *, wire_name: str):
        for _ in range(count):
            current_position = self.get_current_position(wire_name)
            if direction == "L":
                current_position[0] -= 1
            if direction == "D":
                current_position[1] -= 1
            if direction == "R":
                current_position[0] += 1
            if direction == "U":
                current_position[1] += 1

            self.add_path_position(wire_name, tuple(current_position))
            self.set_current_position(wire_name, current_position)

    def shortest_manhattan_distance(self):
        shortest = 0
        for intersection in self.find_intersection_points():
            manhattan_distance = abs(intersection[0]) + abs(intersection[1])
            if manhattan_distance < shortest or not shortest:
                shortest = manhattan_distance
        return shortest

    def shortest_signal_delay(self):
        shortest = 0
        for intersection in self.find_intersection_points():
            signal_delay = self.find_signal_delay(intersection)
            if signal_delay < shortest or not shortest:
                shortest = signal_delay
        return shortest

    def find_signal_delay(self, intersection: tuple):
        delay = 0
        for wire_name in self.wire_grid:
            if intersection not in self.wire_grid[wire_name]["path_positions"]:
                # If we have multiple wires there is no guarantee that each intersection covers all wires
                break

            for path_position in self.wire_grid[wire_name]["path_positions"]:
                delay += 1
                if path_position == intersection:
                    break
        return delay

    def find_intersection_points(self):
        path_position_references = [self.wire_grid[wire_name]["path_positions"] for wire_name in self.wire_grid]

        common_items = set.intersection(*map(set, path_position_references))
        return common_items


class WireDataHandler:
    def __init__(self):
        self.wire_data = WireDataHandler.load_wire_data()

    @staticmethod
    def load_wire_data():
        with open("input.txt") as f:
            return [line.split(",") for line in f.readlines()]

    def get_movement_data(self, wire_name: str):
        for data_piece in self.wire_data[WireDataHandler.get_wire_index(wire_name)]:
            yield WireDataHandler.parse_data_piece(data_piece)

    @staticmethod
    def parse_data_piece(data_piece: str):
        direction = data_piece[0]
        move_count = int(data_piece[1:])
        return direction, move_count

    def get_wire_names(self):
        for index in range(len(self.wire_data)):
            yield WireDataHandler.get_wire_name(index)

    @staticmethod
    def get_wire_name(wire_data_index: int):
        return f"wire_{wire_data_index}"

    @staticmethod
    def get_wire_index(wire_name: str):
        return int(wire_name.split("_")[1])


if __name__ == "__main__":
    _data_handler = WireDataHandler()
    _wire_grid = WireGrid()
    for _wire_name in _data_handler.get_wire_names():
        _wire_grid.add_wire(_wire_name)
        for _direction, _move_count in _data_handler.get_movement_data(_wire_name):
            _wire_grid.move(_direction, _move_count, wire_name=_wire_name)

    print(_wire_grid.shortest_manhattan_distance())
    print(_wire_grid.shortest_signal_delay())
