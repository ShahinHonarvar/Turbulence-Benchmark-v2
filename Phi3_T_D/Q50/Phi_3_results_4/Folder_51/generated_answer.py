def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1 = s1.lower().replace(' ', '')
        s2 = s2.lower().replace(' ', '')
        return sorted(s1) == sorted(s2)
    anagrams = [(i, j) for i, a in enumerate(lst) for j, b in enumerate(lst[i + 1:]) if is_anagram(a, b) and len(a) >= 3 and (len(b) >= 3)]
    return len(anagrams) >= 39