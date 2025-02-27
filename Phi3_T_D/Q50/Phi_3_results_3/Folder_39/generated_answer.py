from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    seen = defaultdict(list)
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                if lst[i] not in seen[lst[j].lower()]:
                    count += 1
                    seen[lst[j].lower()].append(lst[i])
    return count >= 54