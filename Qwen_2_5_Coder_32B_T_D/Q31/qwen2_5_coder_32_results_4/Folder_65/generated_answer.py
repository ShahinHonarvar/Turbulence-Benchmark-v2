def if_perfect_num(numbers):

    def is_perfect(n):
        return sum([i for i in range(1, n) if n % i == 0]) == n
    return is_perfect(numbers[35]) if len(numbers) > 35 else False