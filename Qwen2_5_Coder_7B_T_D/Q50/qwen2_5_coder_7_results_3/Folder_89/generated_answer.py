def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    word_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]
    anagram_pairs = 0
    for group in word_dict.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 36