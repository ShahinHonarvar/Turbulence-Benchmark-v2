def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        word_key = ''.join(sorted(word.lower()))
        if word_key not in anagram_groups:
            anagram_groups[word_key] = [word]
        else:
            anagram_groups[word_key].append(word)
    anagram_counts = [len(group) for group in anagram_groups.values()]
    return sum((1 for count in anagram_counts if count >= 2)) >= 246