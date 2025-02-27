from collections import defaultdict

def generate_anagram_key(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(strings):
    anagram_buckets = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            key = generate_anagram_key(string)
            anagram_buckets[key] += 1
    return sum((count * (count - 1) // 2 for count in anagram_buckets.values())) <= 22