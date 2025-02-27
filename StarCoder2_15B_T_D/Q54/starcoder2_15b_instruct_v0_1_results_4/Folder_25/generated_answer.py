def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_prime(num):
            result.append(num)
            while len(str(num)) > 1:
                num //= 10
                if not is_prime(num):
                    break
            if len(str(num)) == 1:
                result.append(num)
    return sorted(result)