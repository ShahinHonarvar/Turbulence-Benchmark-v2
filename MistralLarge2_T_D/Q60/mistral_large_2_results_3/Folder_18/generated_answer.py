def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[429]
    primes = [str(i) for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)]
    truncatable_primes = []
    for prime in primes:
        temp = prime
        while len(temp) > 1:
            temp = temp[1:-1]
            if not temp or not is_prime(int(temp)):
                break
        else:
            truncatable_primes.append(int(prime))
    return sorted(truncatable_primes, reverse=True)