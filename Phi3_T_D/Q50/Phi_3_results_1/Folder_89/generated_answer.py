import collections

def if_contains_anagrams(strings):
    length_filtered = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_counts = collections.Counter(length_filtered)
    my_counter = collections.Counter()
    for count in anagram_counts.values():
        my_counter[count] += 1
    return sum((x * (x - 1) // 2 for x in my_counter.values())) >= 36