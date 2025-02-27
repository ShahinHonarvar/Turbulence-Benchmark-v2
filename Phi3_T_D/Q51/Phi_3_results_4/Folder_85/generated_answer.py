def if_contains_anagrams(strings):

    def count_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for s in strings:
        if len(s) < 3:
            continue
        key = count_chars(s)
        if key in anagram_count:
            anagram_count[key] += 1
        else:
            anagram_count[key] = 1
    return sum((v for v in anagram_count.values() if v > 1)) <= 276