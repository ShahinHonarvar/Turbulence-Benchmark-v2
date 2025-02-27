def if_perfect_num(numbers):
    if len(numbers) <= 63:
        return False
    n = numbers[63]
    if n < 2:
        return False
    sum_divs = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divs += i
            if i != n // i:
                sum_divs += n // i
    return sum_divs == n