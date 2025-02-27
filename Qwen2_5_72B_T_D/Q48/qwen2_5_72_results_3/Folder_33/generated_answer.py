def return_binary_or_hexa(data):
    if len(data) < 36:
        return ''
    a = data[13]
    b = data[35]
    sum_nums = 0
    for i in range(a + 1, b):
        if i not in data[14:35]:
            sum_nums += i
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:]