def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    word_map = {}
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_map:
                word_map[sorted_word].append(word)
                count += len(word_map[sorted_word]) - 1
            else:
                word_map[sorted_word] = [word]
    return count >= 106