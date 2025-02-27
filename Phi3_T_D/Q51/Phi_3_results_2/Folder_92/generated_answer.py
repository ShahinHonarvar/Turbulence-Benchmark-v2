def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1_map = {}
        for char in s1.lower():
            if char.isalpha() and len(char) >= 3:
                s1_map[char] = s1_map.get(char, 0) + 1
        for char in s2.lower():
            if char.isalpha() and len(char) >= 3:
                if char in s1_map:
                    s1_map[char] -= 1
                    if s1_map[char] == 0:
                        del s1_map[char]
                else:
                    return False
        return len(s1_map) == 0
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 34:
                    return False
    return True