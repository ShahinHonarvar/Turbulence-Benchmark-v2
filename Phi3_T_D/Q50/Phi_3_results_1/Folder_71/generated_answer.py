def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1, str2 = (strings[i].lower(), strings[j].lower())
            if sorted(str1) == sorted(str2) and len(str1) >= 3:
                anagram_count += 1
                if anagram_count >= 57:
                    return True
    return False