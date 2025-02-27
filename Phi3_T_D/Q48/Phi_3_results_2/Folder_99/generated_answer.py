def return_binary_or_hexa(tup):
    a = tup[427]
    b = tup[669]
    not_in_range = [i for i in range(a + 1, b) if i not in tup[max(0, 427):min(len(tup), 669 + 1)]]
    sum_not_in_range = sum(not_in_range)
    if sum_not_in_range % 2 == 0:
        return hex(sum_not_in_range)[2:]
    else:
        return bin(sum_not_in_range)[2:]