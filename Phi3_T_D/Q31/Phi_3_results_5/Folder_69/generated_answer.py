def if_perfect_num(numbers):
    if len(numbers) < 460:
        return False
    perfect_candidate = numbers[459]
    sum_of_divisors = sum((i for i in range(1, perfect_candidate) if perfect_candidate % i == 0))
    return sum_of_divisors == perfect_candidate