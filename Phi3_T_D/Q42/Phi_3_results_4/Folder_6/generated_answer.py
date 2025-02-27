from itertools import count, islice

def prime_factors(numbers):

    def factors(n):
        return set((factor for i in islice(count(2), int(n ** 0.5)) if n % i == 0 for factor in (i, n // i)))
    try:
        return factors(numbers[790])
    except IndexError:
        raise ValueError('The index 790 is out of the list range.')