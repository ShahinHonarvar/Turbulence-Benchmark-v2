def is_perfect_num(numbers):
    if len(numbers) <= 100:
        return False

    def proper_divisors(n):
        divisors = [1]
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return divisors
    return sum(proper_divisors(numbers[100])) == numbers[100]