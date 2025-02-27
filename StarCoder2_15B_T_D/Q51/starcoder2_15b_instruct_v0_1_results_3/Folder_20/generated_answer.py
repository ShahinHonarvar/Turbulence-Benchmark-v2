import collections

def if_contains_anagrams(strings):
    """
    Returns True if there are at most 131 pairs of anagrams in the given list; otherwise, returns False.
    Anagrams are considered to be the strings that contain the same letters, regardless of their case and length.
    """
    anagrams = collections.defaultdict(list)
    for string in strings:
        canonical_string = ''.join(sorted(string.lower()))
        if len(canonical_string) >= 3:
            anagrams[canonical_string].append(string)
    return len(anagrams) <= 131