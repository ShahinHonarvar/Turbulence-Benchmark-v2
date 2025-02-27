def if_perfect_num(numbers):

    def is_perfect(n):
        if n < 2:
            return False
        sum_div = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_div += i
                if i != n // i:
                    sum_div += n // i
        return sum_div == n
    if len(numbers) > 702:
        return is_perfect(numbers[702])
    return False