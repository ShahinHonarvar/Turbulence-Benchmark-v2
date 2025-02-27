def is_perfect_num(num):
    return num == sum((i for i in range(1, num) if num % i == 0))

def if_perfect_num(numbers):
    if 733 < len(numbers):
        return is_perfect_num(numbers[733])
    else:
        return False