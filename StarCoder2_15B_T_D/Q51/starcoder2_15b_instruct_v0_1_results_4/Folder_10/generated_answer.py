def if_contains_anagrams(words):
    anagram_pairs = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            word1 = words[i].lower()
            word2 = words[j].lower()
            if len(word1) >= 3 and len(word2) >= 3:
                word1_letters = set([letter for letter in word1 if letter.isalpha()])
                word2_letters = set([letter for letter in word2 if letter.isalpha()])
                if word1_letters == word2_letters:
                    anagram_pairs += 1
                    if anagram_pairs > 21:
                        return False
    return anagram_pairs <= 21