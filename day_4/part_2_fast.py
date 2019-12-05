import cProfile


def count_valid_passwords(range_start: int, range_end: int):
    return sum(is_password_valid(f"{i}") for i in range(range_start, range_end))


def password_rule_1(password: str):
    """
    Two adjacent digits are the same (like 22 in 122345).
    :param password:
    :return:
    """
    for index in range(len(password)):
        if is_double_and_not_part_of_larger_group(password, index):
            return True
    return False


def password_rule_2(password: str):
    """
    Going from left to right, the digits never decrease; they only ever increase or
    stay the same (like 111123 or 135679).
    :param password:
    :return:
    """
    previous = password[0]
    for char in password:
        if char < previous:
            return False
        previous = char
    return True


def is_double_and_not_part_of_larger_group(password: str, index: int):
    return get_4_characters_surrounding_index(password, index).count(password[index]) == 1


def get_4_characters_surrounding_index(password: str, index: int):
    """
    2 left 2 right
    :param password:
    :param index:
    :return:
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


rules = (password_rule_2, password_rule_1)


def is_password_valid(password: str):
    for rule in rules:
        if not rule(password):
            return False
    return True


def run():
    for i in range(353096, 843212):
        password_rule_2([i])

#cProfile.run("run()")
cProfile.run("print(count_valid_passwords(353096, 843212))")
