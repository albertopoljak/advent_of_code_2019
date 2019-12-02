def load_input_list():
    with open("part_1_input.txt") as f:
        return [int(number) for number in f.read().split(",")]


def get_op_code_parameters(current_index, input_list):
    return input_list[current_index + 1], input_list[current_index + 2], input_list[current_index + 3]


def op_code_instruction(index_1, index_2, result_index, operation: str, input_list):
    if operation == "+":
        input_list[result_index] = input_list[index_1] + input_list[index_2]
    elif operation == "*":
        input_list[result_index] = input_list[index_1] * input_list[index_2]


def get_every_n(n: int, input_list):
    for i in range(0, len(input_list), n):
        yield i, input_list[i]


def get_result_first_index(input_list):
    for index, op_code in get_every_n(4, input_list):
        if op_code == 99:
            break
        elif op_code == 1:
            op_code_instruction(*get_op_code_parameters(index, input_list), "+", input_list)
        elif op_code == 2:
            op_code_instruction(*get_op_code_parameters(index, input_list), "*", input_list)

    return input_list[0]


if __name__ == "__main__":
    _input_list = load_input_list()
    _input_list[1] = 12
    _input_list[2] = 2

    print(get_result_first_index(_input_list))


