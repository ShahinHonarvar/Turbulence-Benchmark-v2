def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            if normalized_word in anagram_count:
                anagram_count[normalized_word] += 1
            else:
                anagram_count[normalized_word] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 73