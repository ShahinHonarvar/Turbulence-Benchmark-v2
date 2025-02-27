def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        if len(word1) != len(word2):
            return False
        count = {}
        for letter in word1:
            if letter not in count:
                count[letter] = 0
            count[letter] += 1
        for letter in word2:
            if letter not in count or count[letter] == 0:
                return False
            count[letter] -= 1
        return True
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 113:
                    return False
    return anagram_pairs <= 113