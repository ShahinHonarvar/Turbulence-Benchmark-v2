def is_perfect_num(number):
    return sum((i for i in range(1, number) if number % i == 0)) == number

def if_perfect_num(lst):
    if len(lst) > 132:
        return is_perfect_num(lst[132])
    return False