from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            count = Counter(lst)
            for key in count:
                if key != s and sorted_s == ''.join(sorted(key.lower())):
                    anagram_count += count[key]
                    break
    return anagram_count >= 178