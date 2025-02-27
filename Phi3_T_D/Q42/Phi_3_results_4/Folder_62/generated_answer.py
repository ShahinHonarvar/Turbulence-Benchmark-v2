def prime_factors(int_list):

    def prime_factors_of_number(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    if len(int_list) > 926:
        number = int_list[926]
        return prime_factors_of_number(number)
    else:
        return 'Index out of range'