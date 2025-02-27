def is_perfect_number(num):
    return num == sum((i for i in range(1, num) if num % i == 0))

def if_perfect_num(numbers):
    if len(numbers) > 74 and is_perfect_number(numbers[74]):
        return True
    else:
        return False