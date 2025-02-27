def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagramPairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (normalize(strings[i]) == normalize(strings[j])):
                anagramPairs.add((normalize(strings[i]), normalize(strings[j])))
    return len(anagramPairs) <= 30