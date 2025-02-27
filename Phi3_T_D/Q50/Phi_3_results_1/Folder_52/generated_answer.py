def if_contains_anagrams(words):
    anagram_count = 0
    sorted_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    for i, word_i in enumerate(sorted_words):
        for j in range(i + 1, len(sorted_words)):
            if word_i == sorted_words[j]:
                anagram_count += 1
                if anagram_count >= 58:
                    return True
    return False