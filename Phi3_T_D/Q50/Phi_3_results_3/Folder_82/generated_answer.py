def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    if len(strings) < 2:
        return False
    freq_map = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = sort_string(s)
        if sorted_str in freq_map and freq_map[sorted_str]:
            freq_map[sorted_str] += 1
        else:
            freq_map[sorted_str] = 1
    return sum((v - 1 for v in freq_map.values() if v - 1 >= 276)) >= 276