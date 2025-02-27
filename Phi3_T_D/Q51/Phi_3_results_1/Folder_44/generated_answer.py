def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    length_sets = {}
    for word in lst:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        length_key = (len(word), normalized)
        if length_key in length_sets:
            anagram_count += length_sets[length_key]
            if anagram_count > 75:
                return False
            length_sets[length_key] += 1
        else:
            length_sets[length_key] = 1
    return True