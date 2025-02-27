from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return len(str1) >= 3 and len(str2) >= 3 and (Counter(str1.lower()) == Counter(str2.lower()))
    anagrams_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagrams_count += 1
                if anagrams_count >= 98:
                    return True
    return False