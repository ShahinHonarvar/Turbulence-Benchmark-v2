def is_perfect_num(num):
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num

def if_perfect_num(numbers):
    if len(numbers) > 87:
        return is_perfect_num(numbers[87])
    return False