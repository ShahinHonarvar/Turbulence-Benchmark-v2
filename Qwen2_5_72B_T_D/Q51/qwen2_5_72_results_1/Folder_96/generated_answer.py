def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    filtered_lst = [normalize(s) for s in lst if len(s) >= 3 and s.isalpha()]
    anagram_counts = {}
    for anagram in filtered_lst:
        anagram_counts[anagram] = anagram_counts.get(anagram, 0) + 1
    pairs = sum((count - 1 for count in anagram_counts.values()))
    return pairs <= 2