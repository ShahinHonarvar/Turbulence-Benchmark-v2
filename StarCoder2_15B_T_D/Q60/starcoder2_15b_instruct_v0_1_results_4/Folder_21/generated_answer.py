def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        is_prime = all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
        is_truncatable = all((int(str(num)[i:]) and int(str(num)[:i + 1]) for i in range(len(str(num)))))
        if is_prime and is_truncatable:
            result.append(num)
    result.sort()
    return result