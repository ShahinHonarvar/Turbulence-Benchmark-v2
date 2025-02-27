def if_contains_anagrams(strings):

    def is_anagram(word1, word2):
        word1 = ''.join((c for c in word1 if c.isalpha())).lower()
        word2 = ''.join((c for c in word2 if c.isalpha())).lower()
        return sorted(word1) == sorted(word2) and len(word1) >= 3
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 96:
                    return False
    return anagram_pairs <= 96