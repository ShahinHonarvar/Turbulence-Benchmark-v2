def all_left_truncatable_prime(nums):
    x = nums[14]
    result = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            temp = num
            while temp > 0:
                digit = temp % 10
                if digit == 0:
                    is_prime = False
                    break
                temp //= 10
            if is_prime:
                result.append(num)
    result.sort(reverse=True)
    return result