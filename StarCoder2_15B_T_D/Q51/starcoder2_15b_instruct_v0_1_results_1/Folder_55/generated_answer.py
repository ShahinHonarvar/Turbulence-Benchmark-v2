def if_contains_anagrams(strings):

    def get_anagrams(strings):
        anagrams = {}
        for string in strings:
            key = ''.join(sorted(string.lower()))
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
        return anagrams

    def group_anagrams_by_length(anagrams):
        anagrams_by_length = {}
        for key, value in anagrams.items():
            length = len(value)
            if length in anagrams_by_length:
                anagrams_by_length[length].append(value)
            else:
                anagrams_by_length[length] = [value]
        return anagrams_by_length

    def check_anagram_pairs(anagrams_by_length):
        anagram_pairs = 0
        for anagrams in anagrams_by_length.values():
            for anagram in anagrams:
                anagram_pairs += len(anagram) // 2
        return anagram_pairs <= 44
    anagrams = get_anagrams(strings)
    anagrams_by_length = group_anagrams_by_length(anagrams)
    return check_anagram_pairs(anagrams_by_length)