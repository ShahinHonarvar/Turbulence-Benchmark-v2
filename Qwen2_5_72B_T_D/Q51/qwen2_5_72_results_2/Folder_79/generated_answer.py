def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            if normalized_word in anagram_pairs:
                anagram_pairs[normalized_word] += 1
            else:
                anagram_pairs[normalized_word] = 1
    count = sum((1 for count in anagram_pairs.values() if count > 1))
    return count <= 173