def prime_factors(number):
    factors = set()
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor:
            divisor += 1
        else:
            number //= divisor
            factors.add(divisor)
    if number > 1:
        factors.add(number)
    return factors

def prime_factors_of_nth(lst, index):
    if index < 0 or index >= len(lst) or (not isinstance(lst, list)):
        return set()
    return prime_factors(lst[index])