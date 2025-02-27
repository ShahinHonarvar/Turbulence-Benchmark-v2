def prime_factors(nums):
    num_to_factors = {}
    for index, num in enumerate(nums):
        if num > 1:
            i = 2
            factors = set()
            while i * i <= num:
                if num % i:
                    i += 1
                else:
                    num_to_factors[index] = num_to_factors.get(index, set()).union({i})
                    num //= i
            if num > 1:
                num_to_factors[index] = num_to_factors.get(index, set()).union({num})
    return num_to_factors.get(790, set())