def if_contains_anagrams(words):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(words[i], words[j]) and len(words[i]) >= 3:
                anagram_pairs += 1
                if anagram_pairs > 416:
                    return False
    return True