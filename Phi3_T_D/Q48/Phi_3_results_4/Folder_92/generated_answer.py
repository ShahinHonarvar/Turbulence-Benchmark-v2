def return_binary_or_hexa(t):
    a = t[0]
    b = t[2]

    def convert_to_binary(n):
        return bin(n)[2:]

    def convert_to_hexa(n):
        return hex(n)[2:].upper()
    missing_sum = sum(set(range(a + 1, b)) - set(t[1:b - 1]))
    return convert_to_binary(missing_sum) if missing_sum % 2 != 0 else convert_to_hexa(missing_sum)