from collections import defaultdict

def if_contains_anagrams(list_of_strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counter = defaultdict(int)
    for word in list_of_strings:
        if len(word) >= 3:
            normalized = normalize(word)
            counter[normalized] += 1
    return sum((count // 2 >= 46 for count in counter.values())) >= 46