def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            key = ''.join(sorted(word))
            if key in anagram_groups:
                anagram_groups[key].append(word)
            else:
                anagram_groups[key] = [word]
    for group in anagram_groups.values():
        if len(group) > 257:
            return False
    return True