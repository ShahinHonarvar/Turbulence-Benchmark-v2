def is_perfect_number(num):
    return sum((i for i in range(1, num) if num % i == 0)) == num

def if_perfect_num(numbers):
    if len(numbers) > 23:
        return is_perfect_number(numbers[23])
    return False