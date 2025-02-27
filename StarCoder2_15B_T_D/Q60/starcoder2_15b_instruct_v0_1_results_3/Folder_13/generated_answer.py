def all_left_right_truncatable_prime(nums):
    x = nums[784]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            if int(str(i)[j + 1:]) % 2 == 0 or int(str(i)[:j + 1]) % 2 == 0:
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes