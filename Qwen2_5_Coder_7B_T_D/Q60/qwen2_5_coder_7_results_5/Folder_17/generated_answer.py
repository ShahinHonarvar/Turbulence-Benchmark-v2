def all_left_right_truncatable_prime(nums):
    x = nums[36]
    primes = [2, 3, 5, 7]
    for num in range(9, x + 1, 2):
        if all((int(digit) % 2 != 0 for digit in str(num))) and all((int(str(num)[:i]) in primes for i in range(1, len(str(num))))) and all((int(str(num)[-i:]) in primes for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)