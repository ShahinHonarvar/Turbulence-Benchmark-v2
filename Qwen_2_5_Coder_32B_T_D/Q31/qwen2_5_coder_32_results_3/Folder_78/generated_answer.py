def if_perfect_num(numbers):

    def is_perfect(n):
        if n < 2:
            return False
        sum_divs = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_divs += i + n // i
        return sum_divs == n
    return is_perfect(numbers[91]) if len(numbers) > 91 else False