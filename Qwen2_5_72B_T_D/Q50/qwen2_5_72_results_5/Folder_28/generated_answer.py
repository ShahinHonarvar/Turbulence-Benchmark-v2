def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    count = 0
    for i, word1 in enumerate(words):
        for word2 in words[i + 1:]:
            if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1) == sorted(word2)):
                count += 1
    return count >= 81