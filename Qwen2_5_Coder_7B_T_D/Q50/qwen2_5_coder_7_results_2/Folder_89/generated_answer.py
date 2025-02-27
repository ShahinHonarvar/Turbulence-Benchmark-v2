def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    pairs = 0
    for word_list in anagrams.values():
        if len(word_list) >= 2:
            pairs += len(word_list) * (len(word_list) - 1) // 2
    return pairs >= 36