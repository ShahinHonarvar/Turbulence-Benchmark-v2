from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return Counter(s.lower())
    sorted_items = sorted(map(normalize, strings))
    unique_anagrams = {}
    for i, item in enumerate(sorted_items):
        for previous_index in range(i):
            if sorted_items[previous_index] == item:
                pair = (min(strings[previous_index], strings[i]), max(strings[previous_index], strings[i]))
                unique_anagrams.setdefault(''.join(sorted(pair[0])) + '-' + ''.join(sorted(pair[1])), 0)
                unique_anagrams['-'.join(sorted(pair))] += 1
    return sum((value for value in unique_anagrams.values() if value >= 1)) <= 61