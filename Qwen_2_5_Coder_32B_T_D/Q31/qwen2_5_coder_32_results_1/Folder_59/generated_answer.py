def if_perfect_num(numbers):
    n = numbers[2]
    total = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n and n != 1