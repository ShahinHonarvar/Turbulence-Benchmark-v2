def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = {}
    for word in lst:
        if len(word) >= 3:
            norm_word = normalize(word)
            if norm_word in count:
                count[norm_word] += 1
            else:
                count[norm_word] = 1
    anagram_pairs = sum((c * (c - 1) // 2 for c in count.values()))
    return anagram_pairs <= 14