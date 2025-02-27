def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for word in lst:
        if len(word) >= 3:
            normalized = normalize_string(word)
            if normalized in anagram_count:
                anagram_count[normalized] += 1
            else:
                anagram_count[normalized] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 48