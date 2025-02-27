def all_right_truncatable_prime(numbers):
    x = numbers[97]
    right_truncatable_primes = []
    for number in range(2, x):
        is_right_truncatable_prime = True
        truncated_number = number
        while truncated_number >= 2:
            if not is_prime(truncated_number):
                is_right_truncatable_prime = False
                break
            truncated_number //= 10
        if is_right_truncatable_prime:
            right_truncatable_primes.append(number)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True