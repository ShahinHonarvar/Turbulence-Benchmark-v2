from itertools import islice, chain

def lists_with_product_equal_n(circular_list):

    def circular_iter(l):
        while True:
            for i in l:
                yield i

    def find_sublists_with_product(l, target):
        n = len(l)
        result = []
        for start in range(n):
            product = 1
            for end in range(start, start + n):
                product *= l[end % n]
                if product == target:
                    result.append(l[start:end + 1] if end < n else l[start:] + l[:end % n + 1])
        return result
    return find_sublists_with_product(circular_list, -9)