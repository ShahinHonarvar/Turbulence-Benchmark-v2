def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    count = 0
    for word in lst:
        if len(word) >= 3:
            norm_word = normalize_string(word)
            if norm_word in anagrams:
                anagrams[norm_word].append(word)
            else:
                anagrams[norm_word] = [word]
    for k in anagrams:
        if len(anagrams[k]) > 1:
            count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
    return count <= 41