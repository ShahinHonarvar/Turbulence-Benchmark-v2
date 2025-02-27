def lists_with_product_equal_n(lst):

    def find_sublists_with_product(arr, target):
        result = []
        n = len(arr)
        for i in range(n):
            product = 1
            for j in range(i, i + n):
                index = j % n
                product *= arr[index]
                if product == target:
                    result.append(arr[i:index + 1])
        return result
    return find_sublists_with_product(lst, -3)