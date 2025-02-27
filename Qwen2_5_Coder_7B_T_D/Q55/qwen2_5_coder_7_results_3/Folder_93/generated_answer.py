def lists_with_product_equal_n(numbers):

    def find_sublists(start, end):
        product = 1
        sublist = []
        for i in range(start, end):
            product *= numbers[i]
            sublist.append(numbers[i])
            if product == -91:
                sublists.append(sublist[:])
                if i + 1 < len(numbers) and numbers[i + 1] == 1:
                    sublists.append(sublist[1:] + [numbers[0]])
                elif i + 1 == len(numbers):
                    sublists.append(sublist[1:])
                product = 1
                sublist = []
            elif product > 91:
                product //= numbers[start]
                sublist = sublist[1:]
    sublists = []
    for i in range(len(numbers)):
        find_sublists(i, len(numbers) + i)
    return sublists