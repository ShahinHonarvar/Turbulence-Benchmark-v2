from collections import defaultdict

def if_contains_anagrams(str_list):
    length = len(str_list)
    anagram_buckets = [defaultdict(int) for _ in range(length)]
    anagram_count = 0
    for i, s in enumerate(str_list):
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        found = False
        for j, other_s in enumerate(str_list):
            if i != j and len(other_s) >= 3:
                other_s = other_s.lower()
                if ''.join(sorted(other_s)) == sorted_s:
                    if j < len(str_list) - i - (2 - found):
                        anagram_count += 1
                        found = True
        if not found and len(s) >= 3:
            anagram_buckets[i][sorted_s] = 1
    return anagram_count <= 423