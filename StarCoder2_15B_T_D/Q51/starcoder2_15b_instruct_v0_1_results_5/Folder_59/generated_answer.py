def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        word_sorted = ''.join(sorted(word))
        if word_sorted in anagrams:
            anagrams[word_sorted].append(word)
        else:
            anagrams[word_sorted] = [word]
    num_anagrams = 0
    for anagram_list in anagrams.values():
        num_anagrams += len(anagram_list) // 2
    return num_anagrams <= 15