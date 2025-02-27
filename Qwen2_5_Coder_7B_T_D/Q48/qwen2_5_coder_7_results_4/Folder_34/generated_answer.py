def return_binary_or_hexa(t):
    a, b = (t[60], t[200])
    required_sum = sum(range(a + 1, b)) - sum(filter(lambda x: a < x < b, t[60:201]))
    if required_sum % 2 == 1:
        return bin(required_sum)[2:]
    else:
        return hex(required_sum)[2:].upper()