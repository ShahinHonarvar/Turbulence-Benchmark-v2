def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    pairs = 0
    for i, s1 in enumerate(strings):
        for s2 in strings[i + 1:]:
            if len(s1) >= 3 and len(s2) >= 3 and are_anagrams(s1, s2):
                pairs += 1
    return pairs >= 96