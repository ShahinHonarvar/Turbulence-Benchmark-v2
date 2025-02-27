def is_perfect_num(num):
    return sum((i for i in range(1, num) if num % i == 0)) == num

def if_perfect_num(numbers):
    return is_perfect_num(numbers[27]) if len(numbers) > 27 else False