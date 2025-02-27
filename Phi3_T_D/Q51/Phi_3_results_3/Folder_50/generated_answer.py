from collections import Counter

def count_anagrams(words):
    hash_map = {}
    for word in words:
        if len(word) >= 3:
            word_hash = ''.join(sorted(word.lower()))
            if word_hash in hash_map:
                hash_map[word_hash] += 1
            else:
                hash_map[word_hash] = 1
    count = sum((v for v in hash_map.values() if v > 1))
    return count

def if_contains_anagrams(words):
    anagrams_count = count_anagrams(words)
    anagram_pairs = anagrams_count * (anagrams_count - 1) // 2
    return anagram_pairs <= 47