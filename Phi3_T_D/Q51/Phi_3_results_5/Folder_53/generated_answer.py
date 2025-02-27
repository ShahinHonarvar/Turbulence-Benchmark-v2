from collections import defaultdict

def if_contains_anagrams(words_list):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    ngrams_count = 0
    word_groups = defaultdict(list)
    for word in words_list:
        if len(word) < 3:
            continue
        word_groups[normalize(word)].append(word)
    for group in word_groups.values():
        ngrams_count += len(group) * (len(group) - 1) // 2
    return ngrams_count <= 8