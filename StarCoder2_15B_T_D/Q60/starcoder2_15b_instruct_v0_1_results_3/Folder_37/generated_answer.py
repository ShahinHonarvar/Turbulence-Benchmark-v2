def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[35]
    result = []
    for num in range(2, x + 1):
        if is_prime(num):
            left, right = (num, num)
            while left >= 10 or right >= 10:
                left = left // 10
                right = right % 10 ** (len(str(right)) - 1)
                if not is_prime(left) or not is_prime(right):
                    break
            else:
                result.append(num)
    result.sort(reverse=True)
    return result