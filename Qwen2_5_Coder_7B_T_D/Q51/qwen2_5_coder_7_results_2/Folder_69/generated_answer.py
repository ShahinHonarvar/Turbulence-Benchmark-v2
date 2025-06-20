from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (Counter(strings[i].lower()) == Counter(strings[j].lower())):
                anagram_count += 1
                if anagram_count > 58:
                    return False
    return True