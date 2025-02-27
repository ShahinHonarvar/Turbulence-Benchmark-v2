def find_subset_of_length_n(elements):
    """
    Returns the number of all subsets of size 32 of a given set of elements.
    """

    def powerset(iterable):
        """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
        s = list(iterable)
        return chain.from_iterable((combinations(s, r) for r in range(len(s) + 1)))
    return sum((1 for _ in filter(lambda x: len(x) == 32, powerset(elements))))