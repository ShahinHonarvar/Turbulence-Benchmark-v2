def if_perfect_num(numbers):

    def is_perfect(n):
        if n < 2:
            return False
        total = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                total += i + n // i
        return total == n
    if len(numbers) > 28:
        return is_perfect(numbers[28])
    return False