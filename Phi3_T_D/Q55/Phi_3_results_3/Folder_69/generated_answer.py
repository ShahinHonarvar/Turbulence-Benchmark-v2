from itertools import cycle, islice
        from itertools import accumulate
        from operator import mul

def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product(sublist):
        cumulative_product = list(accumulate(sublist, mul))
        results = []
        for i in range(len(sublist)):
            for j in range(i + 1, len(cumulative_product)):
                if cumulative_product[j] % cumulative_product[i] == cumulative_product[-1] % cumulative_product[i] == 90:
                    results.append(sublist[i:j + 1])
        return results

    def get_sublists(list_cycle):
        sublists = []
        for start in range(len(list_cycle)):
            sublist = list(islice(cycle(list_cycle), start, None))
            if len(sublist) == len(list_cycle):
                break
            if len(sublist) > 0:
                sublists.extend(find_sublists_with_product(sublist))
        return sublists
    circular_list_cycle = cycle(circular_list)
    sublists = get_sublists(circular_list_cycle)
    seen = set()
    unique_sublists = [sublist for sublist in sublists if tuple(sublist) not in seen and (not seen.add(tuple(sublist)))]
    return unique_sublists