def if_perfect_num(numbers):
    if len(numbers) > 23:
        num = numbers[23]
        divisors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        return sum(divisors) == num
    return False