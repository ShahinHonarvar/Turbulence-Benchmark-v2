def is_perfect_num(num):
    if num < 1:
        return False
    divisors_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:
                divisors_sum += num // i
    return divisors_sum == num

def if_perfect_num(numbers):
    if len(numbers) > 632:
        return is_perfect_num(numbers[632])
    else:
        return False