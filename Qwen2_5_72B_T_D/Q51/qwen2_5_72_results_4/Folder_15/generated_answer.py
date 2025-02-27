def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for item in lst:
        if len(item) >= 3 and item.isalpha():
            normalized = normalize(item)
            anagram_count[normalized] = anagram_count.get(normalized, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 20