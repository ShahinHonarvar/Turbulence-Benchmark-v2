def all_left_right_truncatable_prime(nums):
    x = nums[54]
    primes = set()
    for num in range(2, x + 1):
        if all((int(digit) != 0 and int(str(num)[:i]) in primes and (int(str(num)[i:]) in primes) for i in range(1, len(str(num))))):
            primes.add(num)
    return sorted(filter(lambda num: len(str(num)) > 1, primes))