def if_contains_anagrams(words):
    word_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in word_dict:
            word_dict[sorted_word] = [word]
        else:
            word_dict[sorted_word].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in word_dict.values() if len(v) > 1 and len(v[0]) >= 3))
    return anagram_pairs <= 46