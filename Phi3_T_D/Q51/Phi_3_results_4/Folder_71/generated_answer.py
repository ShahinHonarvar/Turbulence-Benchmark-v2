from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def has_three_or_more_chars(s):
        return len(s) >= 3
    counted_anagrams = defaultdict(int)
    for word in filters(has_three_or_more_chars, strings):
        norm = normalize(word)
        counted_anagrams[norm] += 1
    return sum(counted_anagrams.values()) // 2 <= 9