def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for word in lst:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_count[normalized_word] = anagram_count.get(normalized_word, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 97