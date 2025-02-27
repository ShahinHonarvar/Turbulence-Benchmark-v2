from collections import Counter

def if_contains_anagrams(input_list):
    counter = Counter()
    for string in input_list:
        if len(string) >= 3:
            counter.update([string.lower()])
    return sum((v >= 2 for v in counter.values())) >= 18