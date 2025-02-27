def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    anagram_dict = {}
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            if normalized in anagram_dict:
                anagram_dict[normalized] += 1
                if anagram_dict[normalized] == 2:
                    anagram_pairs += 1
            else:
                anagram_dict[normalized] = 1
    return anagram_pairs >= 86