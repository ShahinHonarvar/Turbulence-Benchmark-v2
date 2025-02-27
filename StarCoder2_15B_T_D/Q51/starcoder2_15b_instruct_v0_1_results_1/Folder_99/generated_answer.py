def if_contains_anagrams(strings):
    anagrams = {}
    for i, string1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            string2 = strings[j]
            if sorted(string1.lower()) == sorted(string2.lower()) and len(string1) >= 3 and (len(string2) >= 3):
                if string1 in anagrams:
                    anagrams[string1].append(string2)
                else:
                    anagrams[string1] = [string2]
    return len(anagrams) <= 93