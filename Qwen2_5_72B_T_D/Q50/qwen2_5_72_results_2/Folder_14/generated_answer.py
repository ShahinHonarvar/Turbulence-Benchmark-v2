from collections import Counter

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    filtered = [s for s in strings if len(s) >= 3]
    normalized_strs = [normalize(s) for s in filtered]
    anagram_counts = Counter(normalized_strs)
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 22