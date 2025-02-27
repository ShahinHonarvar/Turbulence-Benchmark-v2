def if_contains_anagrams(words):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    count = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and is_anagram(words[i], words[j]):
                count += 1
    return count >= 312