def if_contains_anagrams(words):
    anagram_count = 0
    for i, word1 in enumerate(words):
        for j in range(i + 1, len(words)):
            if len(word1) < 3 or len(words[j]) < 3:
                continue
            if sorted(word1.lower()) == sorted(words[j].lower()):
                anagram_count += 1
                if anagram_count > 35:
                    return False
    return True