def is_perfect_num(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

def if_perfect_num(numbers):
    return is_perfect_num(numbers[33]) if len(numbers) > 33 else False