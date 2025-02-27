def prime_factors(lst):

    def factors(n):
        i = 2
        result = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                result.add(i)
        if n > 1:
            result.add(n)
        return result
    return factors(lst[4]) if len(lst) > 4 else set()