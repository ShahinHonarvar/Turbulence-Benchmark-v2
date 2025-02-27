def generate_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return fibonacci

def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci = generate_fibonacci(88)
    if decimal_integer % fibonacci[87] == 0:
        return True
    else:
        return False