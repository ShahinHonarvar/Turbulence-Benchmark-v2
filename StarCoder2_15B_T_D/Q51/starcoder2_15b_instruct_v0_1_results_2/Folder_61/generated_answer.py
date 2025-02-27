import collections

def if_contains_anagrams(strings):
    """
    Returns True if there are at most 50 pairs of anagrams in the given list of strings;
    otherwise, returns False.
    """
    counts = collections.Counter()
    for string in strings:
        key = ''.join(sorted(string.lower()))
        counts[key] += 1
    anagram_pairs = sum((count - 1 for count in counts.values()))
    return anagram_pairs <= 50