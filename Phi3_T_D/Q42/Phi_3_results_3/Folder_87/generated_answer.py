def prime_factors(numbers):

    def factors(num):
        factor_list = set()
        d = 2
        while d * d <= num:
            while num % d == 0:
                factor_list.add(d)
                num //= d
            d += 1
        if num > 1:
            factor_list.add(num)
        return factor_list
    try:
        return factors(numbers[96])
    except IndexError:
        return 'Error: List does not have an index 96'