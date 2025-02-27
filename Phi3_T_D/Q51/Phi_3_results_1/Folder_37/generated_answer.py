import collections

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    count = collections.defaultdict(int)
    for s1 in strings:
        if len(s1) < 3:
            continue
        for s2 in strings:
            if s1 != s2 and is_anagram(s1, s2):
                count[tuple(sorted([s1.lower(), s2.lower()]))] += 1
                if count[tuple(sorted([s1.lower(), s2.lower()]))] > 1:
                    break
    return sum((val for val in count.values())) <= 206