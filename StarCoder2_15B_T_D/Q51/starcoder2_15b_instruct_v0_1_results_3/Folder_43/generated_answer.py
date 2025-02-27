def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    anagram_counts = [len(group) for group in anagram_groups.values()]
    return max(anagram_counts) <= 3