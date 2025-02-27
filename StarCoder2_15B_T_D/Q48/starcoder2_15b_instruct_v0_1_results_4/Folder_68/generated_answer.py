def return_binary_or_hexa(t):
    a, b = (t[0], t[9])
    sum_of_integers = sum(range(a + 1, b))
    sum_of_integers_in_tuple = sum(t[1:9])
    difference = sum_of_integers - sum_of_integers_in_tuple
    if difference % 2 == 1:
        return bin(difference)[2:]
    else:
        return hex(difference)[2:].upper()