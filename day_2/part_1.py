from typing import List, Tuple


def load_integer_list() -> List[int]:
    """
    :return: list of integers separated by commas example [1,0,0,3,99]
    """
    with open("day_2_input.txt") as f:
        return [int(number) for number in f.read().split(",")]


def get_op_code_parameters(current_index: int, input_list: list) -> Tuple[int, int, int]:
    """
    Our instruction format is (all integers): op_code, instruction_parameter_1, i_p_2, i_p_3
    :param current_index: int index from param input_list that represents op_code
    :param input_list: list of ints representing op_codes and their parameters
    :return: tuple of 3 integers, each one of them is instruction parameter of our op_code (param current_index)
    """
    return input_list[current_index + 1], input_list[current_index + 2], input_list[current_index + 3]


def execute_op_code_instruction(index_1: int, index_2: int, result_index: int, operation: str, input_list: list):
    if operation == "+":
        input_list[result_index] = input_list[index_1] + input_list[index_2]
    elif operation == "*":
        input_list[result_index] = input_list[index_1] * input_list[index_2]


def get_every_n(n: int, input_list: list) -> Tuple[int, int]:
    """
    Helper generator function.
    :param n: int, yield every n-th element from param input_list
    :param input_list: list to get elements from
    :return: tuple of 2 ints in form tuple(int, int). Second one is our n-th yielded element from the list and first one
             is the index position of that yielded element in param input_list
    """
    for i in range(0, len(input_list), n):
        yield i, input_list[i]


def get_result_first_index(input_list: list):
    """
    Passes trough the param input_list and executes op_code instructions based on it's parameters.
    OP_CODES:
    99 - stop
    1 - add next 2 arguments together and set input_list[third argument] to that result
    2 - multiply next 2 arguments together and set input_list[third argument] to that result

    :param input_list:
    :return: int, result of executing op_code instructions (the first index of param input_list after execution)
    """
    for index, op_code in get_every_n(4, input_list):
        if op_code == 99:
            break
        elif op_code == 1:
            execute_op_code_instruction(*get_op_code_parameters(index, input_list), "+", input_list)
        elif op_code == 2:
            execute_op_code_instruction(*get_op_code_parameters(index, input_list), "*", input_list)

    return input_list[0]


if __name__ == "__main__":
    _input_list = load_integer_list()
    _input_list[1] = 12
    _input_list[2] = 2

    print(get_result_first_index(_input_list))


