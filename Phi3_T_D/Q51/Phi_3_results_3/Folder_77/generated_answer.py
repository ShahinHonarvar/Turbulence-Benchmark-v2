def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return sorted(s1) == sorted(s2)
    found = set()
    count = 0
    for str1 in strings:
        for str2 in strings:
            if str1 != str2 and len(str1) >= 3 and (len(str2) >= 3) and (str1.lower() not in found) and is_anagram(str1, str2):
                found.add(str1.lower())
                count += 1
                if count > 17:
                    return False
    return True