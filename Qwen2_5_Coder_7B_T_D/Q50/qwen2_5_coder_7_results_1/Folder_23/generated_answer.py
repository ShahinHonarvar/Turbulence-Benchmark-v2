def if_contains_anagrams(lst):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sort_string(lst[i]) == sort_string(lst[j])):
                anagram_count += 1
    return anagram_count >= 67