def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    words = [word.lower() for word in words if len(word) >= 3]
    count = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(words[i], words[j]):
                count += 1
                if count >= 209:
                    return True
    return False