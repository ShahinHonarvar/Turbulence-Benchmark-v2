def is_left_truncatable_prime(n):
    if n < 2 or any((digit == 0 for digit in str(n))):
        return False
    for i in range(len(str(n)) - 1):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    return [num for num in nums if is_left_truncatable_prime(num)]