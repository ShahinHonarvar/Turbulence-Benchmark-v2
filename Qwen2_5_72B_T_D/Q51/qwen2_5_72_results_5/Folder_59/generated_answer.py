def if_contains_anagrams(arr):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_map = {}
    for s in arr:
        if len(s) >= 3 and s.isalpha():
            normalized = normalize(s)
            anagram_map.setdefault(normalized, []).append(s)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_map.values()))
    return anagram_count <= 15