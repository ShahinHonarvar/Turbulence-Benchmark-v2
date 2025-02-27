def if_perfect_num(numbers):

    def is_perfect(num):
        if num < 2:
            return False
        sum_divisors = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_divisors += i + num // i
        return sum_divisors == num
    return is_perfect(numbers[97]) if len(numbers) > 97 else False