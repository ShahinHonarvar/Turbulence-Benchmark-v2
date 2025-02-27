from collections import defaultdict

def if_contains_anagrams(words):
    sorted_words = [''.join(sorted(word.lower())) for word in words]
    word_count = defaultdict(int)
    for word in sorted_words:
        word_count[word] += 1
    count_pairs = sum((1 for count in word_count.values() if count > 1))
    return count_pairs >= 29