def if_contains_anagrams(words):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    words_lower = [word.lower() for word in words if len(word) >= 3]
    for i in range(len(words_lower)):
        for j in range(i + 1, len(words_lower)):
            if are_anagrams(words_lower[i], words_lower[j]):
                count += 1
    return count >= 77