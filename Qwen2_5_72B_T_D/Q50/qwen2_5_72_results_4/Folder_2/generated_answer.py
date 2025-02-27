def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]):
                anagram_pairs += 1
    return anagram_pairs >= 246