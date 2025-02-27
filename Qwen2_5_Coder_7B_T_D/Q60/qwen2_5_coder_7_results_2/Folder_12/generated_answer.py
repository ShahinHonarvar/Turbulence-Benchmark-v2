def all_left_right_truncatable_prime(nums):
    x = nums[70]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if all((int(digit) % 2 != 0 and int(digit) != 5 for digit in str(num))) and all((int(str(num)[:i]) in primes and int(str(num)[-i:]) in primes for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)