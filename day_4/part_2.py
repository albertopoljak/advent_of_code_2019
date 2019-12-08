from day_4.part_1 import password_rule_2
import cProfile
from typing import List


def count_valid_passwords(range_start: int, range_end: int) -> int:
    return sum(is_password_valid(f"{i}") for i in range(range_start, range_end))


def is_password_valid(password: str) -> bool:
    rules = (password_rule_2, password_rule_1)
    return all(rule(password) for rule in rules)


def password_rule_1(password: str) -> bool:
    """
    Two adjacent digits are the same (like 22 in 122345) AND are not part of a larger group of matching digits.
    Examples:

    :param password: str
    :return: bool
    """
    if not password:
        return False

    for index in range(len(password)):
        if is_double_and_not_part_of_larger_group(password, index):
            return True
    return False


def is_double_and_not_part_of_larger_group(password: str, index: int) -> bool:
    return get_4_characters_surrounding_index(password, index).count(password[index]) == 1


def get_4_characters_surrounding_index(password: str, index: int) -> List[str]:
    """
    2 left 2 right
    :param password: str
    :param index: int, index representing index from param password
    :return: list of strings with minimum 2 elements and maximum 4. Elements represent characters from param string
             at index positions [index -2, index -1, index +1, index +2]. If previous/next character is not available
             it is not added (example if index is start position or end position).
    """

    surrounding_chars = []

    if index == 1:
        surrounding_chars.append(password[index - 1])
    elif index > 0:
        surrounding_chars.append(password[index - 1])
        surrounding_chars.append(password[index - 2])

    try:
        surrounding_chars.append(password[index + 1])
        surrounding_chars.append(password[index + 2])
    except IndexError:
        pass

    return surrounding_chars


cProfile.run("print(count_valid_passwords(353096, 843212))")
