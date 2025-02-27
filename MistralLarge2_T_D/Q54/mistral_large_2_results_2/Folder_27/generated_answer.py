def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_right_truncatable_primes(limit):
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            trunc = num
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(num)
    return primes

def all_right_truncatable_prime(nums):
    x = nums[79]
    right_truncatable_primes = get_right_truncatable_primes(x)
    return sorted(right_truncatable_primes, reverse=True)