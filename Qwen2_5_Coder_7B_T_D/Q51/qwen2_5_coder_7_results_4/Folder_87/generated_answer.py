def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3:
                pair = tuple(sorted([strings[i], strings[j]]))
                if pair in anagram_pairs:
                    return False
                anagram_pairs.add(pair)
    return len(anagram_pairs) <= 392