def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    seen = set()
    for word in lst:
        if len(word) < 3:
            continue
        for s in seen:
            if is_anagram(word, s):
                anagram_pairs += 1
                if anagram_pairs > 2:
                    return False
        seen.add(word)
    return anagram_pairs <= 2