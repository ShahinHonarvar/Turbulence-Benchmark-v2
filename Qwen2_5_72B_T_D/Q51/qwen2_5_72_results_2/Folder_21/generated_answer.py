def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            norm = normalize(word)
            count[norm] = count.get(norm, 0) + 1
    anagram_pairs = sum((1 for val in count.values() if val > 1))
    return anagram_pairs <= 26