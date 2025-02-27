from collections import Counter

def if_contains_anagrams(words):
    counts = Counter((len(word) for word in words))
    for length in counts:
        if counts[length] > 1:
            anagram_groups = {}
            for word in words:
                if len(word) == length:
                    key = ''.join(sorted(word.lower()))
                    if key in anagram_groups:
                        anagram_groups[key].append(word)
                    else:
                        anagram_groups[key] = [word]
            for group in anagram_groups.values():
                if len(group) > 1:
                    return True
    return False