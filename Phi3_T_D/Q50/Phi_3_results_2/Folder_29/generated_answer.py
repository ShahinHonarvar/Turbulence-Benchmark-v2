from collections import defaultdict

def if_contains_anagrams(strings):
    len_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            len_map[len(s)].append(sorted_s)
    count_pairs = 0
    for lengths in len_map.values():
        seen = set()
        for sorted_str in lengths:
            if sorted_str in seen:
                count_pairs += 1
                if count_pairs >= 35:
                    return True
            else:
                seen.add(sorted_str)
    return False