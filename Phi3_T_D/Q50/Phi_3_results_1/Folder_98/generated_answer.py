def if_contains_anagrams(lst):

    def get_sorted_tuple(s):
        return tuple(sorted(s.lower()))
    anagrams_count = 0
    seen = set()
    for string in lst:
        if len(string) >= 3:
            sorted_tuple = get_sorted_tuple(string)
            if sorted_tuple in seen:
                anagrams_count += 1
            else:
                seen.add(sorted_tuple)
    return anagrams_count >= 7