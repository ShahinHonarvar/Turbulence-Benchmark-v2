def is_perfect_num(numbers):
    if 247 < len(numbers):
        n = numbers[247]
        divisors = [1]
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                divisors.append(n // i)
        return sum(divisors) == n
    return False