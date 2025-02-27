def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[77]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and '0' not in str(num):
            temp = str(num)
            while len(temp) > 1:
                if not is_prime(int(temp[1:-1])):
                    break
                temp = temp[1:-1]
            else:
                primes.append(num)
    return sorted(primes, reverse=True)