def if_contains_anagrams(words):
    anagram_pairs = 0
    for i, word in enumerate(words):
        for j in range(i + 1, len(words)):
            if sorted(word.lower()) == sorted(words[j].lower()) and len(word) >= 3:
                anagram_pairs += 1
    return anagram_pairs >= 20