def if_perfect_num(numbers):

    def is_perfect(n):
        s = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                s += i
                if i != n // i:
                    s += n // i
        return n == s
    return is_perfect(numbers[85]) if len(numbers) > 85 else False