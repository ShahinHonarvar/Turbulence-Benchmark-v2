def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and is_anagram(words[i], words[j]):
                count += 1
                if count >= 189:
                    return True
    return False