def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[73]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and '0' not in str(num):
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    break
                temp = int(str(temp)[1:-1] or '0')
            else:
                primes.append(num)
    primes.sort(reverse=True)
    return primes