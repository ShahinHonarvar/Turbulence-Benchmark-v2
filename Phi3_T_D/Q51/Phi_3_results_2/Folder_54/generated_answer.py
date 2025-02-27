from collections import defaultdict

def if_contains_anagrams(str_list):
    count = defaultdict(int)
    for s in str_list:
        if len(s) >= 3:
            count[''.join(sorted(s.lower()))] += 1
    return sum((value / 2 for value in count.values())) <= 39