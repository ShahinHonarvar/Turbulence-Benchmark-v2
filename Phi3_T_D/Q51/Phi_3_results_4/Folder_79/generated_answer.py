def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word)).lower()
    counted = {}
    anagram_count = 0
    for word in words:
        if len(word) < 3:
            continue
        norm_word = normalize(word)
        if norm_word in counted:
            anagram_count += counted[norm_word] * (counted[norm_word] - 1) // 2
            counted[norm_word] += 1
        else:
            counted[norm_word] = 1
    return anagram_count <= 173