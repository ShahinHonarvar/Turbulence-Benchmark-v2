def lists_with_product_equal_n(numbers):

    def find_sublists(start, target_product, numbers):
        n = len(numbers)
        result = []
        current_product = 1
        for i in range(n):
            current_product *= numbers[(start + i) % n]
            if current_product == target_product:
                result.append(numbers[start:start + i + 1])
            if current_product != 0 and abs(current_product) > abs(target_product):
                break
        return result
    n = len(numbers)
    all_sublists = []
    for i in range(n):
        all_sublists.extend(find_sublists(i, -69, numbers))
    return all_sublists