def return_binary_or_hexa():

    def value_exists(arr, start, end, value):
        return any((value == arr[i] for i in range(start, end + 1)))

    def sum_missing_values(arr, start, end):
        total = 0
        for num in range(arr[start] + 1, arr[end]):
            if not value_exists(arr, start, end, num):
                total += num
        return total

    def to_binary_string(num):
        return bin(num).replace('0b', '')

    def to_hexa_string(num):
        return hex(num).replace('0x', '')
    a = 45
    b = 48
    try:
        total = sum_missing_values(arr, a, b)
        if total % 2 == 0:
            return to_hexa_string(total)
        else:
            return to_binary_string(total)
    except IndexError:
        return ''