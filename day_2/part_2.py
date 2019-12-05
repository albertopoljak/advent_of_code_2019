import itertools
from day_2 import part_1


original_list = part_1.load_integer_list()


for noun, verb in itertools.product(range(100), list(reversed(range(100)))):
    copy_list = [x for x in original_list]
    copy_list[1] = noun
    copy_list[2] = verb
    try:
        if part_1.get_result_first_index(copy_list) == 19690720:
            print("Correct result is for", noun, ",", verb)
            break
    except IndexError:
        continue
