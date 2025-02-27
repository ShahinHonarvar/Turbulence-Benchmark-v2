def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3:
                anagram_pairs += 1
                if anagram_pairs > 206:
                    return False
    return True