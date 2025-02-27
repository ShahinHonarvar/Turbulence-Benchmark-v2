def lists_with_product_equal_n(circular_list):

    def circular_subarrays(arr, length):
        subarrays = []
        for start in range(len(arr)):
            subarray = [arr[(start + i) % len(arr)] for i in range(length)]
            subarrays.append(subarray)
        return subarrays
    all_sublists = []
    for length in range(1, len(circular_list) + 1):
        subarrays = circular_subarrays(circular_list, length)
        for subarray in subarrays:
            product = 1
            for num in subarray:
                product *= num
            if product == 45:
                all_sublists.append(subarray)
    return all_sublists