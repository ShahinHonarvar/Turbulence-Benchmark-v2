def return_binary_or_hexa(t):

    def is_present(number):
        return any((57 <= i <= 84 and t[i] == number for i in range(len(t))))
    a, b = (t[57], t[84])
    total_sum = sum((i for i in range(a + 1, b) if not is_present(i)))
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]