def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[803]
    result = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        left_right = str(num)
        right_left = str(num)
        is_truncatable = True
        while len(left_right) > 1:
            left_right = left_right[1:-1]
            right_left = right_left[1:-1]
            if not is_prime(int(left_right)) or not is_prime(int(right_left)):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            result.append(num)
    return result