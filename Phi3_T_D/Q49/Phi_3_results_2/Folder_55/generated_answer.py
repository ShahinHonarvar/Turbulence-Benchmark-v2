def if_decimal_is_divisible(binary_string):

    def find_fibonacci_number_39():
        a, b = (0, 1)
        for _ in range(38):
            a, b = (b, a + b)
        return b
    decimal_number = int(binary_string, 2)
    fibonacci_39 = find_fibonacci_number_39()
    return decimal_number % fibonacci_39 == 0