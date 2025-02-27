def if_contains_anagrams(strings):

    def str_to_tuple(s):
        return tuple(sorted((c for c in s.lower() if c.isalpha() and len(s) >= 3)))
    anagrams_count = {}
    for s in strings:
        key = str_to_tuple(s)
        if key in anagrams_count:
            anagrams_count[key] += 1
        else:
            anagrams_count[key] = 1
    return sum((count * (count - 1) // 2 for count in anagrams_count.values())) <= 58