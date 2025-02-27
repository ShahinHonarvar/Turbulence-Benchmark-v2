import collections

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                first_counter = collections.Counter(strings[i].lower())
                second_counter = collections.Counter(strings[j].lower())
                if first_counter == second_counter:
                    anagram_pairs += 1
                    if anagram_pairs > 116:
                        return False
    return anagram_pairs <= 116