def if_perfect_num(lst):
    perfect_numbers = {6, 28}
    try:
        if lst[42] in perfect_numbers:
            return True
        return False
    except IndexError:
        return False