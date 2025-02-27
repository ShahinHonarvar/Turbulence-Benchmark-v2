def if_perfect_num(lst):
    perfect_nums = [6, 28, 496, 8128, 33550336]
    if len(lst) > 59 and lst[60] in perfect_nums:
        return True
    return False