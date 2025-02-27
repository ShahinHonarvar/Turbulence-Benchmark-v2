def if_perfect_num(numbers):

    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    try:
        return is_perfect(numbers[45]) if len(numbers) > 45 else False
    except IndexError:
        return False