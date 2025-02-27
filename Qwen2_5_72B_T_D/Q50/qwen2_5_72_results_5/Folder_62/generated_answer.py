def if_contains_anagrams(words):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    words = [word.lower() for word in words if len(word) >= 3]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if are_anagrams(words[i], words[j]):
                count += 1
                if count >= 43:
                    return True
    return False