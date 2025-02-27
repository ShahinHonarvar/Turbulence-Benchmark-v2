def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagrams_dict = {}
    anagram_count = 0
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            if normalized in anagrams_dict:
                anagram_count += anagrams_dict[normalized]
                anagrams_dict[normalized] += 1
            else:
                anagrams_dict[normalized] = 1
    return anagram_count >= 22