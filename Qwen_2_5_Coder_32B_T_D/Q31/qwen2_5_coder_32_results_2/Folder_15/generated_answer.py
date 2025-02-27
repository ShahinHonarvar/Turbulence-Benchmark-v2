def if_perfect_num(numbers):

    def is_perfect(n):
        if n < 2:
            return False
        sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum += i + n // i
        return sum == n
    return is_perfect(numbers[10]) if len(numbers) > 10 else False