def lists_with_product_equal_n(numbers):

    def find_sublists(start):
        product = 1
        sublists = []
        for end in range(start, len(numbers) + start):
            product *= numbers[end % len(numbers)]
            if product == -82:
                sublists.append(numbers[start:end % len(numbers)])
            elif product % -82 == 0:
                break
        return sublists
    result = []
    for i in range(len(numbers)):
        result.extend(find_sublists(i))
    return result