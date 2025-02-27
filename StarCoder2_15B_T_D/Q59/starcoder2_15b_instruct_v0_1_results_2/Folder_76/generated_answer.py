def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    result = []
    for i in range(2, nums[370]):
        if is_prime(i):
            num_str = str(i)
            is_left_truncatable = True
            for j in range(len(num_str) - 1):
                if not is_prime(int(num_str[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                result.append(i)
    result.sort(reverse=True)
    return result