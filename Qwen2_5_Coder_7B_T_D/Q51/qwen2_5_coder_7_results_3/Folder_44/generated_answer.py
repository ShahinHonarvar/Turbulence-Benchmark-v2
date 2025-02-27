def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3:
                count += 1
    return count <= 75