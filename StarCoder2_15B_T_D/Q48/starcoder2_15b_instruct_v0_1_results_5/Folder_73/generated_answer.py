def return_binary_or_hexa(tup, a=10, b=76):
    s = set(tup)
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in s:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        result = bin(sum_of_integers)[2:]
    else:
        result = hex(sum_of_integers)[2:]
    return result