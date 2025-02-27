def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        if sorted(s1) == sorted(s2) and len(s1) >= 3:
            return True
        return False
    pairs = [(s1, s2) for i, s1 in enumerate(strings) for s2 in strings[i + 1:] if is_anagram(s1, s2)]
    return len(pairs) <= 147