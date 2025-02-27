def if_perfect_num(numbers):

    def is_perfect(num):
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    if len(numbers) > 126:
        return is_perfect(numbers[126])
    return False