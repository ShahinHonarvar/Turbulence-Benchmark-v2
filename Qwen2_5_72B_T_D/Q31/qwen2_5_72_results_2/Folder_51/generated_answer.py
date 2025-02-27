def if_perfect_num(numbers):

    def is_perfect(n):
        sum = 1
        for x in range(2, n):
            if n % x == 0:
                sum += x
        return sum == n
    return is_perfect(numbers[64]) if len(numbers) > 64 else False