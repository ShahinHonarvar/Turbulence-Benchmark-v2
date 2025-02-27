def if_contains_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    count_pairs = sum((len(v) // 2 for v in anagram_dict.values()))
    return count_pairs >= 60