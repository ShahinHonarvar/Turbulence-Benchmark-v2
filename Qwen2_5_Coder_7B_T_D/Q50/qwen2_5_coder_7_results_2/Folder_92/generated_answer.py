def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    word_counts = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_counts:
                word_counts[sorted_word] += 1
                if word_counts[sorted_word] == 2:
                    return True
            else:
                word_counts[sorted_word] = 1
    return False