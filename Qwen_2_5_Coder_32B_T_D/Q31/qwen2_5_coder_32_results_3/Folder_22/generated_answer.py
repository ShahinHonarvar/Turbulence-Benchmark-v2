def if_perfect_num(numbers):

    def is_perfect(n):
        total = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
        return total == n
    return is_perfect(numbers[72]) if len(numbers) > 72 else False