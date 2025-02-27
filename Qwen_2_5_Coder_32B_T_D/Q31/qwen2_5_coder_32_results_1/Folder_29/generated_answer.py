def if_perfect_num(numbers):

    def is_perfect(n):
        sum1 = 0
        for i in range(1, n):
            if n % i == 0:
                sum1 += i
        return sum1 == n
    return is_perfect(numbers[19]) if len(numbers) > 19 else False