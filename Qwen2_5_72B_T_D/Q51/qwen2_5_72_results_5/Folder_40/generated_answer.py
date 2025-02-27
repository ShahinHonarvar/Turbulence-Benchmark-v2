def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = {}
    for word in words:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_count[normalized_word] = anagram_count.get(normalized_word, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 29