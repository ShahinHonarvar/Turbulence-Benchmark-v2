import collections

def if_contains_anagrams(words):
    anagram_groups = collections.defaultdict(list)
    for word in words:
        canonical_form = ''.join(sorted(word.lower()))
        anagram_groups[canonical_form].append(word)
    anagram_counts = [len(group) for group in anagram_groups.values() if len(group) >= 3]
    return sum(anagram_counts) <= 70