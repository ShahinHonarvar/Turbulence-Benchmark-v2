def if_contains_anagrams(strings):

    def normalize(s):
        return sorted(s.lower())
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            norm = normalize(string)
            anagram_key = ''.join(norm)
            if anagram_key in anagrams:
                anagrams[anagram_key].append(string)
            else:
                anagrams[anagram_key] = [string]
    count = 0
    for lst in anagrams.values():
        if len(lst) > 1:
            count += len(lst) * (len(lst) - 1) // 2
    return count >= 77