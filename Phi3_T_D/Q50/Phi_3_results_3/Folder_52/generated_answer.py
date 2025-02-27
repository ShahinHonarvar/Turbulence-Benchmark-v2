from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    anagram_dict = defaultdict(set)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                if lst[j] in anagram_dict[lst[i]]:
                    count += 1
                else:
                    anagram_dict[lst[i]].add(lst[j])
                    count += 1
                if count >= 58:
                    return True
    return False