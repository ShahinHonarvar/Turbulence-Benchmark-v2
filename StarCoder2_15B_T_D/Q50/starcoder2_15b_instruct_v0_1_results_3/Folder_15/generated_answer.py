def if_contains_anagrams(input_list):
    anagrams = {}
    for word in input_list:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    anagram_pairs = sum((len(v) - 1 for v in anagrams.values() if len(v) > 1))
    return anagram_pairs >= 4