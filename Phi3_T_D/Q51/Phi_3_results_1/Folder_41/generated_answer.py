def if_contains_anagrams(strings):

    def normalize(s, case_insensitive=True):
        return ''.join(sorted(s)) if case_insensitive else s
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) in checked_pairs:
                continue
            if all((len(s) >= 3 for s in (strings[i], strings[j]))) and normalize(strings[i].lower()) == normalize(strings[j].lower()):
                anagram_count += 1
                checked_pairs.add((i, j))
                checked_pairs.add((j, i))
    return anagram_count <= 52