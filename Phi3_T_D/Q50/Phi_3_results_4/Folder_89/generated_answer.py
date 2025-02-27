from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    filtered_lst = [s for s in lst if len(s) >= 3]
    length_dict = defaultdict(list)
    for item in filtered_lst:
        sorted_item = ''.join(sorted(item.lower()))
        length_dict[len(item)].append(sorted_item)
    anagram_pairs = 0
    for sorted_items in length_dict.values():
        seen_items = set()
        for item in sorted_items:
            if item in seen_items:
                anagram_pairs += 1
            else:
                seen_items.add(item)
    return anagram_pairs >= 36