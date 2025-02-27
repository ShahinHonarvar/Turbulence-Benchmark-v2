def all_left_right_truncatable_prime(nums):
    x = nums[792]
    primes = set()
    for num in range(2, x + 1):
        if all((int(digit) != 0 and all((int(digit) != 0 for digit in str(num)[:i + 1])) and all((int(digit) != 0 for digit in str(num)[-i - 1:])) and all((int(digit) != 0 for digit in str(num)[-i - 1:])) and all((int(digit) != 0 for digit in str(num)[-i - 1:])) for i in range(len(str(num))))):
            primes.add(num)
    return sorted(list(primes))