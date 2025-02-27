def if_contains_anagrams(words):

    def are_anagrams(word1, word2):
        word1 = ''.join((c for c in word1 if c.isalpha())).lower()
        word2 = ''.join((c for c in word2 if c.isalpha())).lower()
        return sorted(word1) == sorted(word2) and len(word1) >= 3
    anagram_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if are_anagrams(words[i], words[j]):
                anagram_count += 1
    return anagram_count <= 84