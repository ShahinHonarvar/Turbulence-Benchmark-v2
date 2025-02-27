from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_buckets = defaultdict(list)
    anagram_count = 0
    for s in strings:
        s_strip = s.lower().replace(' ', '')
        if len(s_strip) >= 3:
            sorted_s = ''.join(sorted(s_strip))
            anagram_buckets[sorted_s].append(s)
    for sorted_s in anagram_buckets:
        if len(anagram_buckets[sorted_s]) >= 2:
            anagram_count += len(anagram_buckets[sorted_s]) // 2
    return anagram_count >= 19