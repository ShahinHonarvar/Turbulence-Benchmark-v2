def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            normalized_word = normalize(word)
            if normalized_word in anagram_dict:
                anagram_dict[normalized_word] += 1
            else:
                anagram_dict[normalized_word] = 1
    anagram_counts = [count for count in anagram_dict.values() if count >= 2]
    return sum(anagram_counts) >= 6