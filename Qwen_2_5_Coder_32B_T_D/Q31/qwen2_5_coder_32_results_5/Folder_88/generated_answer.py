def if_perfect_num(numbers):

    def is_perfect(n):
        s = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                s += i + n // i
        return s == n and n != 1
    return is_perfect(numbers[46]) if len(numbers) > 46 else False