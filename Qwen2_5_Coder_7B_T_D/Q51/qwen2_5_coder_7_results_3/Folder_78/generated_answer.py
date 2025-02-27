from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    processed = set()
    for i in range(len(lst)):
        if lst[i] not in processed and len(lst[i]) >= 3:
            sorted_str = ''.join(sorted(lst[i].lower()))
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3 and ''.join(sorted(lst[j].lower())) == sorted_str:
                    anagram_pairs += 1
                    processed.add(lst[j])
            processed.add(lst[i])
    return anagram_pairs <= 70