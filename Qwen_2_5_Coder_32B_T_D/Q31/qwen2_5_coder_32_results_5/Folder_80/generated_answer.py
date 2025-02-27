def if_perfect_num(numbers):

    def is_perfect(num):
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    return is_perfect(numbers[746]) if len(numbers) > 746 else False