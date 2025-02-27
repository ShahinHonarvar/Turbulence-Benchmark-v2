from collections import defaultdict

def if_contains_anagrams(strings):
    size_dict = defaultdict(list)
    count = 0
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        size_dict[sorted_str].append(s)
    for anagrams in size_dict.values():
        if len(anagrams) > 1 and len(anagrams[0]) >= 3:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 73