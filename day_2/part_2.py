import itertools
from day_2 import part_1


original_list = part_1.load_input_list()


for x, y in itertools.product(range(100), list(reversed(range(100)))):
    copy_list = [x for x in original_list]
    copy_list[1] = x
    copy_list[2] = y
    try:
        if part_1.get_result_first_index(copy_list) == 19690720:
            print("Correct result is for", x, ",", y)
            break
    except IndexError:
        continue
