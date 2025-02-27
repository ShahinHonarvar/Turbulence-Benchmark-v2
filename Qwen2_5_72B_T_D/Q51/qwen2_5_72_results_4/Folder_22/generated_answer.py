def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            normalized_word = normalize(word)
            if normalized_word in anagrams:
                anagrams[normalized_word].append(word)
            else:
                anagrams[normalized_word] = [word]
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return anagram_pairs <= 14