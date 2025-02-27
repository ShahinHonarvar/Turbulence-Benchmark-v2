def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return sorted(s1.lower()) == sorted(s2.lower())
    pairs = [(s, t) for i, s in enumerate(strings) for t in strings[i + 1:] if are_anagrams(s, t)]
    return len(pairs) <= 89