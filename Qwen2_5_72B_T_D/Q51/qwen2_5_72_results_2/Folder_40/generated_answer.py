def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if normalize(strings[i]) == normalize(strings[j]):
                    anagram_pairs.add((min(strings[i], strings[j]), max(strings[i], strings[j])))
    return len(anagram_pairs) <= 29