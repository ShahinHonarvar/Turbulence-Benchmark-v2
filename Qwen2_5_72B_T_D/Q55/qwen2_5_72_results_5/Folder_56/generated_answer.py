def lists_with_product_equal_n(circular_list):

    def circular_subarrays(arr):
        n = len(arr)
        subarrays_with_product(arr, n)

    def subarrays_with_product(arr, n):
        result = []
        for i in range(n):
            product = 1
            for j in range(i, i + n):
                product *= arr[j % n]
                if product == -65:
                    result.append(arr[i:j % n + 1])
                elif product < -65:
                    break
        return result
    return circular_subarrays(circular_list)