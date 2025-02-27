def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for word in lst:
        if len(word) >= 3:
            norm_word = normalize(word)
            anagram_count[norm_word] = anagram_count.get(norm_word, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return anagram_pairs <= 14