def all_right_truncatable_prime(nums):
    x = nums[25]
    truncatable_primes = []
    for number in range(2, x):
        is_truncatable_prime = True
        for i in range(1, len(str(number))):
            truncated_number = int(str(number)[:-i])
            if truncated_number < 2 or not is_prime(truncated_number):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True