def if_contains_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    anagram_pairs = sum((len(value) > 1 for value in anagram_dict.values()))
    return anagram_pairs <= 50