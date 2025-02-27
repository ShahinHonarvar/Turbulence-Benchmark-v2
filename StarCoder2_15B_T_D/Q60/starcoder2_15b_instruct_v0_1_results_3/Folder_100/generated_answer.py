def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums: tuple) -> list:
    x = nums[26]
    truncatable_primes = []
    for num in range(11, x + 1):
        if not is_prime(num):
            continue
        truncated_num = num
        while truncated_num >= 10:
            truncated_num = int(str(truncated_num)[1:])
            if not is_prime(truncated_num):
                break
        else:
            truncated_num = num
            while truncated_num >= 10:
                truncated_num = int(str(truncated_num)[:-1])
                if not is_prime(truncated_num):
                    break
            else:
                truncatable_primes.append(num)
    truncatable_primes.sort()
    return truncatable_primes