def if_perfect_num(numbers):
    if len(numbers) < 4:
        return False
    perfect_number = numbers[3]
    divisors_sum = sum([i for i in range(1, perfect_number) if perfect_number % i == 0])
    return divisors_sum == perfect_number