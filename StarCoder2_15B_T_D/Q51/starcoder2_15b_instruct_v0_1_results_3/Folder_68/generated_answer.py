from collections import Counter

def if_contains_anagrams(words):
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                word1_letters = Counter(words[i].lower())
                word2_letters = Counter(words[j].lower())
                if word1_letters == word2_letters:
                    anagram_pairs += 1
                    if anagram_pairs > 94:
                        return False
    return anagram_pairs <= 94