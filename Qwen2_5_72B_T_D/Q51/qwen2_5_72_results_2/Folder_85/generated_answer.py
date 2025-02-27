def if_contains_anagrams(lst):

    def to_key(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for word in lst:
        if len(word) >= 3:
            key = to_key(word)
            anagram_count[key] = anagram_count.get(key, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 276