from collections import Counter

def if_contains_anagrams(strings):

    def are_anagrams(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    count = 0
    strings = [s for s in strings if len(s) >= 3]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                count += 1
                if count > 21:
                    return False
    return True