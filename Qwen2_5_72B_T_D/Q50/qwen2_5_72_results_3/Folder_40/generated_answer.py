def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_map = {}
    for item in lst:
        if len(item) >= 3:
            normalized = normalize(item)
            anagram_map[normalized] = anagram_map.get(normalized, 0) + 1
    count = 0
    for value in anagram_map.values():
        if value > 1:
            count += value - 1
        if count >= 3:
            return True
    return False