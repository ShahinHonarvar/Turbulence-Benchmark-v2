from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            sorted_s = ''.join(sorted(s))
            counter = Counter(lst)
            for other in lst:
                if other != s and other.lower() == sorted_s and (counter[other] > 1):
                    anagram_count += 1
    return anagram_count >= 81