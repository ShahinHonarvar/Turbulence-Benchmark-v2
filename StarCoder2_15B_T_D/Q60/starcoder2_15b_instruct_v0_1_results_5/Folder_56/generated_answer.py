def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    left_right_truncatable_primes = []
    for num in nums:
        if num <= 1 or str(num).startswith('0'):
            continue
        temp = str(num)
        while len(temp) >= 2:
            if not is_prime(int(temp)):
                break
            temp = temp[1:-1]
        else:
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)