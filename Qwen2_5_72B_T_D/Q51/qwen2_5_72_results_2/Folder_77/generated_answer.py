def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for word in lst:
        if len(word) >= 3:
            normalized_word = normalize(word)
            if normalized_word in anagram_count:
                anagram_count[normalized_word] += 1
            else:
                anagram_count[normalized_word] = 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs_count <= 17