def if_contains_anagrams(word_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    n = len(word_list)
    for i in range(n):
        for j in range(i + 1, n):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3 and is_anagram(word_list[i], word_list[j]):
                count += 1
    return count >= 92