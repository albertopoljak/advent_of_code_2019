def count_valid_passwords(range_start: int, range_end: int):
    return sum(is_password_valid(str(i)) for i in range(range_start, range_end))


def is_password_valid(password: str):
    rules = (password_rule_1, password_rule_2)
    return all(rule(password) for rule in rules)


def password_rule_1(password: str):
    """
    Two adjacent digits are the same (like 22 in 122345).
    :param password:
    :return:
    """
    if not password:
        return False

    for index, char in enumerate(password):
        if char in get_characters_surrounding_index(password, index):
            return True
    return False


def get_characters_surrounding_index(password: str, index: int):
    surrounding_chars = []

    if index > 0:
        surrounding_chars.append(password[index - 1])

    try:
        surrounding_chars.append(password[index + 1])
    except IndexError:
        pass

    return surrounding_chars


def password_rule_2(password: str):
    """
    Going from left to right, the digits never decrease; they only ever increase or
    stay the same (like 111123 or 135679).
    :param password:
    :return:
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
