from collections import defaultdict

def if_contains_anagrams(lst):
    sorted_anagrams = defaultdict(list)
    for item in lst:
        if len(item) >= 3:
            sorted_item = ''.join(sorted(item.lower()))
            sorted_anagrams[sorted_item].append(item)
    count_pairs = 0
    checked_items = set()
    for anagram_list in sorted_anagrams.values():
        for item in anagram_list:
            pairings = [x for x in checked_items if sorted(x.lower()) == ''.join(sorted(item.lower())) and x != item]
            count_pairs += len(pairings)
            for paired_item in pairings:
                checked_items.add(item)
                checked_items.add(paired_item)
    return count_pairs >= 14