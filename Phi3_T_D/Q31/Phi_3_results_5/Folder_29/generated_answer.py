def if_perfect_num(numbers):
    if 19 < len(numbers) and is_perfect(numbers[19]):
        return True
    else:
        return False

def is_perfect(num):
    return num > 0 and num == sum((i for i in range(1, num) if num % i == 0))