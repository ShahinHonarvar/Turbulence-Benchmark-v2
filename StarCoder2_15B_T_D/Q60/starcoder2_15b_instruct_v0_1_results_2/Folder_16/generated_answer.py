def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if not is_prime(num):
            continue
        is_truncatable = True
        for i in range(len(str(num)) - 1):
            left_trunc = int(str(num)[i + 1:])
            right_trunc = int(str(num)[:len(str(num)) - i - 1])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    result.sort()
    return result