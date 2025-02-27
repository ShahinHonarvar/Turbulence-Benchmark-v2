from itertools import cycle

def lists_with_product_equal_n(lst):

    def find_sublists(lst):
        results = []
        n = 32
        for i in range(len(lst)):
            product = 1
            temp_sublist = []
            for j in range(i, len(lst) + i):
                temp_sublist.append(lst[j % len(lst)])
                product *= lst[j % len(lst)]
                if product > n:
                    break
                if product == n:
                    results.append(temp_sublist)
        return results
    return find_sublists(lst)