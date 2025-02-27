def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def check_anagrams(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        return normalize(str1) == normalize(str2)
    count_anagrams = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if check_anagrams(lst[i], lst[j]):
                count_anagrams += 1
    return count_anagrams >= 75