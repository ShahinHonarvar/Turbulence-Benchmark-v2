def lists_with_product_equal_n(numbers):
    result = []
    n = len(numbers)
    for i in range(n):
        product = 1
        window = []
        for j in range(i, i + n):
            index = j % n
            product *= numbers[index]
            window.append(numbers[index])
            if product == 27:
                result.append(window.copy())
            elif product > 27:
                product //= numbers[i]
                window.pop(0)
    return result