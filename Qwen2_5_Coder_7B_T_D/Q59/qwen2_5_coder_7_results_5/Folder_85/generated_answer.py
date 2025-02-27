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

def all_left_truncatable_prime(nums):
    x = nums[94]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(11, x, 2):
        if is_prime(num):
            str_num = str(num)
            if '0' not in str_num:
                left_truncatable = True
                for i in range(len(str_num)):
                    if not is_prime(int(str_num[i:])):
                        left_truncatable = False
                        break
                if left_truncatable:
                    primes.append(num)
    primes.sort()
    return primes