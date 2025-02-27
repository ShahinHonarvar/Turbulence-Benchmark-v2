def if_contains_anagrams(arr):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_map = {}
    for word in arr:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_map[normalized_word] = anagram_map.get(normalized_word, 0) + 1
    anagram_count = sum((count * (count - 1) // 2 for count in anagram_map.values()))
    return anagram_count <= 38