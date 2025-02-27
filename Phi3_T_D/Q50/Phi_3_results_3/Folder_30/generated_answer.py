from collections import defaultdict

def if_contains_anagrams(words):
    anagrams_count = 0
    word_buckets = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_buckets[sorted_word].append(word)
    for bucket in word_buckets.values():
        anagrams_count += len(bucket) * (len(bucket) - 1) // 2
    return anagrams_count >= 78