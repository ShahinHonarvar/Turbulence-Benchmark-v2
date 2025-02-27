from collections import Counter

def count_unique_characters(string):
    return len(Counter(string.lower()))

def are_anagrams(string1, string2):
    return count_unique_characters(string1) == count_unique_characters(string2)

def if_contains_anagrams(string_list):
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if sorted(string_list[i].lower()) == sorted(string_list[j].lower()) and (string_list[i].lower(), string_list[j].lower()) not in checked_pairs:
                    anagram_count += 1
                    checked_pairs.add((string_list[i].lower(), string_list[j].lower()))
    return anagram_count <= 21