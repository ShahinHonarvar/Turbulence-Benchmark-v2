def if_contains_anagrams(input_list):
    sorted_words = {}
    for word in input_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word not in sorted_words:
            sorted_words[sorted_word] = [word]
        else:
            sorted_words[sorted_word].append(word)
    anagram_count = 0
    for anagrams in sorted_words.values():
        if len(anagrams) > 1:
            anagram_count += len(anagrams) - 1
    return anagram_count <= 74