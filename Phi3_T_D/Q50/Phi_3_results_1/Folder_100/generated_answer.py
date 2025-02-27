def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        anagrams[sorted_str] = anagrams.get(sorted_str, 0) + 1
    count_pairs = sum((1 for v in anagrams.values() if v >= 2))
    valid_count = sum((v // 2 for v in anagrams.values() if v >= 3))
    return count_pairs >= 95 or valid_count >= 47