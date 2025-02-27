def if_contains_anagrams(lst):

    def anagram_key(s):
        return ''.join(sorted(s.lower()))
    filtered_anagrams = dict()
    for word in lst:
        if len(word) >= 3:
            key = anagram_key(word)
            if key in filtered_anagrams:
                filtered_anagrams[key] += 1
            else:
                filtered_anagrams[key] = 1
    anagram_pairs = sum(filtered_anagrams.values()) // 2
    return anagram_pairs <= 4