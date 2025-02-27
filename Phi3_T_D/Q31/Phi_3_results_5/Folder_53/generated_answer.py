def is_perfect_num(num):
    return num == sum([i for i in range(1, num) if num % i == 0])

def if_perfect_num(ints):
    return is_perfect_num(ints[73]) if len(ints) > 73 else False