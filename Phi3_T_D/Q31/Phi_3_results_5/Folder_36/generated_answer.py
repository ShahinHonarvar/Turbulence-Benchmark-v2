def is_perfect_num(num):
    """
    Helper function to check if a number is perfect.
    A number is perfect if the sum of its proper divisors is equal to the number itself.
    """
    if num == 1:
        return False
    divisors_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:
                divisors_sum += num // i
    return divisors_sum == num

def if_perfect_num(numbers):
    return is_perfect_num(numbers[990]) if len(numbers) > 990 else False