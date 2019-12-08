from typing import List


def count_valid_passwords(range_start: int, range_end: int) -> int:
    return sum(is_password_valid(str(i)) for i in range(range_start, range_end))


def is_password_valid(password: str) -> bool:
    rules = (password_rule_1, password_rule_2)
    return all(rule(password) for rule in rules)


def password_rule_1(password: str) -> bool:
    """
    At least one occurrence of: Two adjacent digits are the same (like 22 in 122345).
    :param password: str
    :return: bool
    """
    if not password:
        return False

    for index, char in enumerate(password):
        if char in get_characters_surrounding_index(password, index):
            return True
    return False


def get_characters_surrounding_index(password: str, index: int) -> List[str]:
    """
    :param password: str
    :param index: int, index representing index from param password
    :return: list in form [str, optional str] where first index is character before the param index and the second is the
             character after the param index. If previous/next character is not available it is not added (example if
             index is start position or end position)
    """

    surrounding_chars = []

    if index > 0:
        surrounding_chars.append(password[index - 1])

    try:
        surrounding_chars.append(password[index + 1])
    except IndexError:
        pass

    return surrounding_chars


def password_rule_2(password: str) -> bool:
    """
    Check if going from left to right, the digits never decrease; they only ever increase or
    stay the same (like 111123 or 135679).
    :param password: str
    :return: bool
    """
    if not password:
        return False

    previous = password[0]
    for char in password:
        if char < previous:
            return False
        previous = char
    return True


if __name__ == "__main__":
    print(count_valid_passwords(353096, 843212))
