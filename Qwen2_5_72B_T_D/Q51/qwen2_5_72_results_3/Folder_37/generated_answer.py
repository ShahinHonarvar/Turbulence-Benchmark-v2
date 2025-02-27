def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = {}
    for word in words:
        if len(word) >= 3 and word.isalpha():
            norm = normalize(word)
            anagram_count[norm] = anagram_count.get(norm, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 206