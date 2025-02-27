def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_pairs = []
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs.append((strings[i], strings[j]))
    return len(anagram_pairs) <= 41