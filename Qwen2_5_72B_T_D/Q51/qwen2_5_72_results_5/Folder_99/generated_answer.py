def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for word in lst:
        if len(word) >= 3:
            norm = normalize(word)
            if norm in anagram_count:
                anagram_count[norm] += 1
            else:
                anagram_count[norm] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 93