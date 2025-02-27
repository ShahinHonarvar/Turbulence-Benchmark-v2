def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            normalized_word = normalize(word)
            if normalized_word in anagram_dict:
                anagram_dict[normalized_word].append(word)
            else:
                anagram_dict[normalized_word] = [word]
    anagram_count = sum((1 for group in anagram_dict.values() if len(group) > 1))
    return anagram_count >= 2