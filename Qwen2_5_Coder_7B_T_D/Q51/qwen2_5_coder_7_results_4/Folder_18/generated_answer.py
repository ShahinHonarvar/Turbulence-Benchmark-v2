def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    considered = set()
    for i in range(len(lst)):
        if i in considered:
            continue
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagram_pairs += 1
                considered.add(j)
                if anagram_pairs > 42:
                    return False
    return True