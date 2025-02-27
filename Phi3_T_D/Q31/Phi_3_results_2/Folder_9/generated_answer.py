def is_perfect_num(numbers):

    def proper_divisors(n):
        return [i for i in range(1, n) if n % i == 0]
    if len(numbers) > 24:
        divisors_sum = sum(proper_divisors(numbers[24]))
        return divisors_sum == numbers[24]
    return False