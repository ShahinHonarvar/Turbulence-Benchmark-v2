def lists_with_product_equal_n(numbers, n):
    result = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers) + i):
            sublist = numbers[i:j]
            if len(sublist) > len(numbers):
                break
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result