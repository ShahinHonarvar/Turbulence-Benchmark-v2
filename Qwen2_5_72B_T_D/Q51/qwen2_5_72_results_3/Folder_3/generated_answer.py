def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = {}
    for word in words:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            if normalized_word in anagram_count:
                anagram_count[normalized_word] += 1
            else:
                anagram_count[normalized_word] = 1
    pair_count = 0
    for count in anagram_count.values():
        pair_count += count * (count - 1) // 2
        if pair_count > 66:
            return False
    return True