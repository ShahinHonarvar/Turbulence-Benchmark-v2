def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    seen = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            if normalized_word in seen:
                seen[normalized_word] += 1
                if seen[normalized_word] == 2:
                    anagram_count += 1
            else:
                seen[normalized_word] = 1
    return anagram_count <= 131