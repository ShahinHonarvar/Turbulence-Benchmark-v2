def if_contains_anagrams(words):

    def canonical(word):
        word_chars = sorted(word.lower())
        return ''.join(word_chars)
    unique = {}
    for word in words:
        length_three = len(word) >= 3
        if length_three:
            key = canonical(word)
            if key in unique:
                unique[key].append(word)
            else:
                unique[key] = [word]
    anagram_pairs = 0
    for anagram_list in unique.values():
        num_words = len(anagram_list)
        if num_words > 1:
            anagram_pairs += num_words * (num_words - 1) // 2
        if anagram_pairs > 407:
            return False
    return True