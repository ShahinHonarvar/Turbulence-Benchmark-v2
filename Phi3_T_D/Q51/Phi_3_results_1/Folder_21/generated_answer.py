import collections

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return len(s1) >= 3 and len(s2) >= 3 and (collections.Counter(s1) == collections.Counter(s2))
    pairs = [(s, t) for idx, s in enumerate(strings) for t in strings[idx + 1:] if is_anagram(s, t)]
    return len(pairs) <= 26