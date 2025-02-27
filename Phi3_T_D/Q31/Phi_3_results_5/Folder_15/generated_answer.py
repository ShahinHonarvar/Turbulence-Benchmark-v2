def if_perfect_num(numbers):

    def is_perfect(num):
        sum_divisors = sum([i + num // i for i in range(1, int(num ** 0.5) + 1) if num % i == 0])
        return num == sum_divisors - num
    return is_perfect(numbers[10]) if len(numbers) > 10 else False