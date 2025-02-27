def if_contains_anagrams(string_list):

    def are_anagrams(s1, s2):
        if len(s1) != len(s2):
            return False
        s1, s2 = (s1.lower(), s2.lower())
        count = {}
        for char in s1:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in s2:
            if char in count:
                count[char] -= 1
                if count[char] < 0:
                    return False
            else:
                return False
        return True
    anagram_count = 0
    n = len(string_list)
    for i in range(n):
        for j in range(i + 1, n):
            if are_anagrams(string_list[i], string_list[j]):
                anagram_count += 1
                if anagram_count >= 73:
                    return True
    return False