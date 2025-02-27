def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def remove_single_letters(words):
        return [word for word in words if len(word) > 2]
    words = remove_single_letters(words)
    sorted_words = sorted(words, key=lambda x: sorted(x.lower()))
    count = 0
    i = 0
    while i < len(sorted_words) - 1:
        j = i + 1
        while j < len(sorted_words) and is_anagram(sorted_words[i], sorted_words[j]):
            j += 1
        if j - i > 1:
            count += j - i - 1
        i = j
    return count <= 9