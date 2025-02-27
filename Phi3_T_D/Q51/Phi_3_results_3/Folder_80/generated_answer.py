def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3)
    counts = {}
    for word in lst:
        word_key = ''.join(sorted(word.lower()))
        if word_key in counts:
            counts[word_key] += 1
        else:
            counts[word_key] = 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in counts.values()))
    return anagram_pairs <= 255