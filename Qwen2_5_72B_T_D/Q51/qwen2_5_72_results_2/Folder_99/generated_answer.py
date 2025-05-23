def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_count[normalized_word] = anagram_count.get(normalized_word, 0) + 1
    pairs = 0
    for count in anagram_count.values():
        pairs += count * (count - 1) // 2
        if pairs > 93:
            return False
    return True