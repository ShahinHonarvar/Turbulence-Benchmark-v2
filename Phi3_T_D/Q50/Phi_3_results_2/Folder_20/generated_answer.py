from collections import Counter

def if_contains_anagrams(string_list):
    count_map = {}
    for s in string_list:
        s = s.lower()
        if len(s) >= 3:
            s_count = Counter(sorted(s))
            if s_count in count_map:
                count_map[s_count].append(s)
            else:
                count_map[s_count] = [s]
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in count_map.values()))
    return anagram_pairs >= 64