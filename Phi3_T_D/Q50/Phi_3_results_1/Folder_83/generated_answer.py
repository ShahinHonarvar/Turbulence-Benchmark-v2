from collections import defaultdict

def if_contains_anagrams(words):
    word_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_groups[sorted_word].append(word)
    total_pairs = sum((len(group) * (len(group) - 1) // 2 for group in word_groups.values()))
    return total_pairs >= 48