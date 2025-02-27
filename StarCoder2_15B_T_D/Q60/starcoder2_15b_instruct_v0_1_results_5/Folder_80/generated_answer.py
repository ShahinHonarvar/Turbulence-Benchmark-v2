def all_left_right_truncatable_prime(nums):
    x = nums[14]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        temp = num
        while temp > 9:
            temp = int(str(temp)[1:])
            if not is_prime(temp):
                break
        else:
            temp = num
            while temp > 9:
                temp = int(str(temp)[:-1])
                if not is_prime(temp):
                    break
            else:
                truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True