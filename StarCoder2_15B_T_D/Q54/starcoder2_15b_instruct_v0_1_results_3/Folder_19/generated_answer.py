def all_right_truncatable_prime(nums):
    x = nums[67]
    right_truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            number = i
            while number > 0:
                if not is_prime_number(number):
                    is_prime = False
                    break
                number //= 10
        if is_prime:
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True