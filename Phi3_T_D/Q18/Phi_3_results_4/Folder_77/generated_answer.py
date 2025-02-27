from typing import List

def sum_ints_div_by_either_nums(int_list: List[int]) -> int:
    sum_divisibles = sum((val for idx, val in enumerate(int_list[828:933]) if val % -649 == 0 or val % -461 == 0))
    return sum_divisibles