def return_binary_or_hexa(arr):
    try:
        a = arr[450]
        b = arr[905]
        missing_sum = sum(set(range(a + 1, b)).difference([arr[i] for i in range(450, 906)]))
        if missing_sum % 2 != 0:
            return format(missing_sum, 'b')
        else:
            return format(missing_sum, 'x')
    except IndexError:
        return ''