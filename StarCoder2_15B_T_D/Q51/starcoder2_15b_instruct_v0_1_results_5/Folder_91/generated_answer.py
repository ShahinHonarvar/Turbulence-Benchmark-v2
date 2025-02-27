def if_contains_anagrams(words):
    anagram_pairs = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            word1 = sorted(words[i].lower())
            word2 = sorted(words[j].lower())
            if word1 == word2 and len(words[i]) >= 3 and (len(words[j]) >= 3):
                anagram_pairs += 1
    return anagram_pairs <= 88