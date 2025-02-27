def return_binary_or_hexa(arr):
    sum_of_missing = sum(set(range(arr[38] + 1, arr[52])).difference(arr[38:53]))
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]