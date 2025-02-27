def is_perfect_num(integers):
    if len(integers) > 68 and is_perfect(integers[68]):
        return True
    return False

def is_perfect(n):
    sum_divisors = sum([i for i in range(1, n) if n % i == 0])
    return sum_divisors == n