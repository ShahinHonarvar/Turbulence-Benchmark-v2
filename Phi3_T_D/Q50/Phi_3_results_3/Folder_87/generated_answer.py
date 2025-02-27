from collections import defaultdict

def if_contains_anagrams(lst):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    sorted_dict = defaultdict(int)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            first = sort_string(lst[i])
            second = sort_string(lst[j])
            if first == second and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                anagram_count += 1
            sorted_dict[first] += 1
    return anagram_count >= 88