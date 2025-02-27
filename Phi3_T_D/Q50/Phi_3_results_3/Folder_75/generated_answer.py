from collections import defaultdict
import itertools

def if_contains_anagrams(lst):
    count = 0
    length_three_and_up = filter(lambda s: len(s) >= 3, lst)
    sorted_words = [''.join(sorted(word.lower())) for word in length_three_and_up]
    anagrams = defaultdict(list)
    for key, group in itertools.groupby(sorted(sorted_words)):
        if len(group) > 1:
            anagrams[key].extend(list(group))
    for _, items in anagrams.items():
        pairs = itertools.combinations(items, 2)
        count += sum((1 for _ in pairs))
    return count >= 70