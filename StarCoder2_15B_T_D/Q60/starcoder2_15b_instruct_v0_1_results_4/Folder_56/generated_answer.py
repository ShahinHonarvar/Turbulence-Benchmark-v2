def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums: tuple) -> list:
    x = nums[30]
    truncatable_primes = []
    for num in range(2, x + 1):
        if not is_prime(num):
            continue
        truncatable = True
        remaining_num = num
        while remaining_num >= 10:
            remaining_num = remaining_num // 10
            if not is_prime(remaining_num):
                truncatable = False
                break
        if not truncatable:
            continue
        remaining_num = num
        while remaining_num >= 10:
            remaining_num = remaining_num % 10 ** (len(str(remaining_num)) - 1)
            if not is_prime(remaining_num):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.append(num)
    truncatable_primes.sort()
    return truncatable_primes