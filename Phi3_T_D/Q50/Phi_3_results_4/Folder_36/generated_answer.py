from collections import defaultdict

def if_contains_anagrams(words):
    length_filtered = [word.lower() for word in words if len(word) >= 3]
    sorted_words = [''.join(sorted(word)) for word in length_filtered]
    anagram_buckets = defaultdict(list)
    for word in sorted_words:
        anagram_buckets[word].append(length_filtered[sorted_words.index(word)])
    count_anagrams = sum((1 for bucket in anagram_buckets.values() if len(bucket) > 1))
    return count_anagrams >= 312