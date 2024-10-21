from typing import Union

my_list: list = [1, 2, 3, 4, 5]
my_tuple: tuple = (1, 2, 3, 4, 5)
my_set: set = {1, 2, 3, 4, 5}
my_kw: dict = {1: "张三", 2: "里斯"}


def add(x: int, y: int) -> int:
    return x + y


new_list: list[Union[str, int]] = [1, "2", 3]

new_kw: dict[int, Union[str, int]] = {1: "张三", 2: "里斯"}


def sub(x: int, y: int) -> Union[int, str]:
    return x - y
