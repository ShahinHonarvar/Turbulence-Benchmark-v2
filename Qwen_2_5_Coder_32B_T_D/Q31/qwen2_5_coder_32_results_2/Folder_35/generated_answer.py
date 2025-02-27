def if_perfect_num(numbers):

    def is_perfect(num):
        if num < 2:
            return False
        sum_divisors = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_divisors += i
                if i != num // i:
                    sum_divisors += num // i
        return num == sum_divisors
    return is_perfect(numbers[993]) if len(numbers) > 993 else False