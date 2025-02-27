def if_contains_anagrams(lst):
    anagram_groups = {}
    for i, word in enumerate(lst):
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(i)
        else:
            anagram_groups[sorted_word] = [i]
    for anagrams in anagram_groups.values():
        if len(anagrams) > 366:
            return False
    return True