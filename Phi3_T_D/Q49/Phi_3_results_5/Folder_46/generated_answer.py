def if_decimal_is_divisible(binary_str):

    def binary_to_decimal(bstr):
        return int(bstr, 2)

    def fib_modulo(divisor, cache={}):
        if divisor in cache:
            return cache[divisor]
        if divisor in (0, 1):
            cache[divisor] = divisor
            return divisor
        cache[divisor] = fib_modulo(divisor - 1, cache) + fib_modulo(divisor - 2, cache)
        return cache[divisor] % divisor
    decimal_number = binary_to_decimal(binary_str)
    fibonacci_139th = fib_modulo(139)
    return decimal_number % fibonacci_139th == 0