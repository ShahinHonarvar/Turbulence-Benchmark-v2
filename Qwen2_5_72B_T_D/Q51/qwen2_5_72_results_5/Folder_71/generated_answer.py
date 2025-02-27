def if_contains_anagrams(lst):

    def canonical(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for word in lst:
        if len(word) >= 3:
            canon = canonical(word)
            anagram_count[canon] = anagram_count.get(canon, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 9