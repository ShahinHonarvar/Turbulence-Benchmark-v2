from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                counter1 = Counter(strings[i].lower())
                counter2 = Counter(strings[j].lower())
                if counter1 == counter2:
                    anagram_pairs += 1
                    if anagram_pairs > 21:
                        return False
    return anagram_pairs <= 21