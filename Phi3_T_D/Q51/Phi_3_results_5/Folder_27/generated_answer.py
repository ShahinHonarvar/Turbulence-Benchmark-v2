from collections import defaultdict

def if_contains_anagrams(strings):

    def clean_string(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    anagram_buckets = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            bucket_key = clean_string(string)
            anagram_buckets[bucket_key].append(string)
    anagram_pairs = sum((len(words) * (len(words) - 1) // 2 for words in anagram_buckets.values()))
    return anagram_pairs <= 113