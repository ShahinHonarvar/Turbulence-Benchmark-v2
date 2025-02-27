def if_perfect_num(integers):
    if 53 < len(integers):
        num = integers[53]
        divisors_sum = sum([i for i in range(1, num) if num % i == 0])
        return divisors_sum == num
    return False