def if_contains_anagrams(strings):

    def get_sorted_tuple(s):
        return tuple(sorted((c.lower() for c in s if c.isalpha())))
    sorted_strings = [get_sorted_tuple(s) for s in strings if len(s) >= 3]
    return sum((sorted_strings.count(t) * (sorted_strings.count(t) - 1) // 2 for t in set(sorted_strings))) <= 36