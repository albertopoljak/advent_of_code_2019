class StarMap:
    def __init__(self):
        """
        Values are star objects names
        Keys are start objects name that are being directly orbited by dict value(also star object name)
        {directly_orbiting_object_name: object_name}
        """
        self.star_chart = {}

    def add_star_object(self, directly_orbiting_object_name: str, space_object_name: str):
        self.star_chart[directly_orbiting_object_name] = space_object_name

    def count_orbits(self, space_object_name: str) -> int:
        """
        :param space_object_name: str, we start from this and count orbits to first object in start chart (COM).
        :return: int, total orbits to the first (in this case COM aka universal Center of Mass) star object.
        """
        count = 0
        next_object_name = space_object_name

        while True:
            try:
                current_object = self.star_chart[next_object_name]
                count += 1
                next_object_name = self.star_chart[current_object]
                count += 1
            except KeyError:
                return count

    def count_orbital_transfers(self, start_object: str, end_object: str) -> int:
        """
        The idea is to get direct route of all objects from specified object to the one that is at the start of star
        chart. We get that as list of strings and we do it for both parameters, both the start_object and end_object.
        Then, since both lead to start of star chart THERE HAS to be a common element where they paths intersect.
        So we just take the distance between that specified object (both start_object and end_object) and the
        first common element and sum those 2 values.
        :param start_object: str
        :param end_object: str
        :return: int, total orbital transfers
        """
        first_object_direct_route = self._get_route_to_start(start_object)
        second_object_direct_route = self._get_route_to_start(end_object)
        # find the first common item
        common = None
        for object in first_object_direct_route:
            if object in second_object_direct_route:
                common = object
                break

        return first_object_direct_route.index(common) + second_object_direct_route.index(common)

    def _get_route_to_start(self, space_object_name: str) -> list:
        """
        Get's all object names that are in direct route from our object to the star chart start object
        """
        direct_route = []
        next_object_name = space_object_name

        while True:
            try:
                current_object = self.star_chart[next_object_name]
                direct_route.append(current_object)
                next_object_name = self.star_chart[current_object]
                direct_route.append(next_object_name)
            except KeyError:
                return direct_route


if __name__ == "__main__":
    star_map = StarMap()

    with open("part_1_2_input.txt") as f:
        data = [line.strip() for line in f.readlines()]

    for line in data:
        directly_orbiting_name, object_name = line.split(")")
        star_map.add_star_object(object_name, directly_orbiting_name)

    #part_1
    total = 0
    for key in star_map.star_chart:
        total += star_map.count_orbits(key)
    print(total)


    #part_2
    print(star_map.count_orbital_transfers("YOU", "SAN"))
