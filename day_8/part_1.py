from typing import Union, List, Tuple


def yield_every_n(iterable: Union[str, list, tuple], chunks: int):
    for i in range(0, len(iterable), chunks):
        yield(iterable[i:i+chunks])


def find_layer_with_fewest_0_digits(image_data: List[List]) -> int:
    index_of_layer_with_fewest_0 = 0
    fewest_0 = 0
    for layer_index, layer in enumerate(image_data):
        current_layer_0_count = _count_specific_digits(layer, "0")
        if fewest_0 == 0 or current_layer_0_count < fewest_0:
            fewest_0 = current_layer_0_count
            index_of_layer_with_fewest_0 = layer_index

    return index_of_layer_with_fewest_0


def _count_specific_digits(input_list: List[str], digit: str) -> int:
    count = 0
    for string in input_list:
        count += string.count(digit)
    return count


def find_color_of_layers(layer_colors: Tuple[str]) -> str:
    """
    Layer colors represent a list of strings where each string represents color. First element in color a TOP (first)
    layer while last it the color of bottom (last) layer.

    Function will return top-most color that isn't transparent.
    """
    for color in layer_colors:
        if color in ("0", "1"):
            return color


if __name__ == "__main__":
    image_width = 25
    image_height = 6

    with open("input.txt") as f:
        data = f.read()

    _image_data = [[layer_row for layer_row in yield_every_n(full_layer, image_width)] for full_layer in yield_every_n(data, image_width*image_height)]

    # part_1
    _layer_index = find_layer_with_fewest_0_digits(_image_data)
    _layer = _image_data[_layer_index]
    print(_count_specific_digits(_layer, "1") * _count_specific_digits(_layer, "2"))

    # part_2
    final_image = []

    for image_layers in zip(*_image_data):
        temp_list = []
        for _layer_colors in zip(*image_layers):
            temp_list.append(find_color_of_layers(_layer_colors))
        final_image.append("".join(temp_list))

    print("\n".join(final_image).replace("0", " "))
