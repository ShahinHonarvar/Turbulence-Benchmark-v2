from collections import defaultdict

def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        if len(s1) != len(s2) or len(s1) < 3:
            return False
        count = defaultdict(int)
        for char in s1:
            count[char] += 1
        for char in s2:
            if count[char] == 0:
                return False
            count[char] -= 1
        return True
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]):
                count += 1
                if count >= 77:
                    return True
    return False