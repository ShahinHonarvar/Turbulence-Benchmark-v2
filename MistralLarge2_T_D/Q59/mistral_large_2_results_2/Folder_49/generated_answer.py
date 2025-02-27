def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[14]
    primes = []
    for num in range(2, x):
        if is_prime(num) and '0' not in str(num):
            is_trunc_prime = True
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    is_trunc_prime = False
                    break
                temp = int(str(temp)[1:])
            if is_trunc_prime:
                primes.append(num)
    return sorted(primes)