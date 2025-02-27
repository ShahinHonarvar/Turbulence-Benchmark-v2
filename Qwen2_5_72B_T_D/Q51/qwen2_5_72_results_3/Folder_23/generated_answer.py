def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_groups = {}
    for word in lst:
        if len(word) < 3:
            continue
        norm_word = normalize(word)
        if norm_word in anagram_groups:
            anagram_groups[norm_word].append(word)
            if len(anagram_groups[norm_word]) == 2:
                anagram_count += 1
                if anagram_count > 49:
                    return False
        else:
            anagram_groups[norm_word] = [word]
    return True