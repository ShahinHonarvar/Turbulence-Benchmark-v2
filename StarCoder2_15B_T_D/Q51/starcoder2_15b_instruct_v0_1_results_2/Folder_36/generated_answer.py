import collections

def if_contains_anagrams(words):
    anagram_groups = collections.defaultdict(list)
    for word in words:
        canonical_word = ''.join(sorted(word.lower()))
        anagram_groups[canonical_word].append(word)
    return len([group for group in anagram_groups.values() if len(group) >= 3]) <= 25