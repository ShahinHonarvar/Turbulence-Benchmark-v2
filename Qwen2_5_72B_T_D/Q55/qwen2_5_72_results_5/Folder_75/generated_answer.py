def lists_with_product_equal_n(circular_list):
    n = 13
    result = []
    length = len(circular_list)

    def circular_subarrays(arr, start, end, first):
        if start % length == end and start != 0:
            return
        if start < length:
            current = 1
            for i in range(start, end):
                index = i % length
                current *= arr[index]
                if current == n:
                    result.append(arr[start % length:end % length if end % length > start % length else length] + arr[:end % length if end % length < start % length else 0])
        if first and end == start + length:
            return
        if first:
            for m in range(length):
                circular_subarrays(arr, m, m, False)
        else:
            circular_subarrays(arr, start, end + 1, False)
    circular_subarrays(circular_list, 0, 0, True)
    return result