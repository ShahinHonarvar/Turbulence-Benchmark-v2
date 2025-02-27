def if_contains_anagrams(words):

    def count_letters(word):
        return tuple(sorted(word.lower()))
    anagram_pairs = 0
    length_threshold = 3
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= length_threshold and len(words[j]) >= length_threshold:
                if count_letters(words[i]) == count_letters(words[j]):
                    anagram_pairs += 1
                    if anagram_pairs >= 68:
                        return True
    return False