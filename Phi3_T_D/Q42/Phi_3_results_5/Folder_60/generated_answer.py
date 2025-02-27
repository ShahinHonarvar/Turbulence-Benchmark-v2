def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def factors(n):
        result = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    result.add(i)
                if is_prime(n // i):
                    result.add(n // i)
        return result
    try:
        return factors(nums[88])
    except IndexError:
        return 'List does not have 89 elements'