from itertools import cycle

def lists_with_product_equal_n(nums):

    def find_sublists(head, tail, product, result):
        contiguous_nums = [head]
        while head != tail:
            head = next(c)
            if sum(contiguous_nums) == 0 or next(c) == 0 or product % next(c) != 0:
                yield None
                head = next(tailcycle)
                contiguous_nums = [head]
            else:
                product //= next(c)
                contiguous_nums.append(next(c))
                if product == 1:
                    yield tuple((startnum for startnum in contiguous_nums if startnum))
                    head = next(c)
                    contiguous_nums = [head]
        yield None

    def circular():
        if not nums:
            return
        c = cycle(nums)
        while True:
            yield next(c)
    tailcycle = circular()
    found_sublists = set()
    for startnum in nums:
        tail = next(tailcycle)
        for sublist in find_sublists(startnum, tail, -65, result=None):
            if sublist is not None:
                if min(sublist) * max(sublist) == -65:
                    found_sublists.add(sublist)
    return [list(s) for s in found_sublists]