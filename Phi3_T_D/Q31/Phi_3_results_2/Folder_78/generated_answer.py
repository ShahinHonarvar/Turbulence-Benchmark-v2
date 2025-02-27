def is_perfect_number(num):
    return num == sum((i for i in range(1, num) if num % i == 0))

def if_perfect_num(numbers):
    return numbers[91] if len(numbers) > 91 and is_perfect_number(numbers[91]) else False