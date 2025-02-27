def if_contains_anagrams(strings):

    def string_signature(s):
        s = s.lower()
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return tuple(sorted(freq.items()))
    string_sets = {}
    for s in strings:
        signature = string_signature(s)
        if signature in string_sets:
            string_sets[signature].append(s)
        else:
            string_sets[signature] = [s]
    anagram_pairs = 0
    for value in string_sets.values():
        pairs = sum(range(len(value)))
        anagram_pairs += pairs
        if anagram_pairs > 206:
            return False
    return True