from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_counter = 0
    for index, string in enumerate(strings):
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            for other in strings[index + 1:]:
                if len(other) == len(string):
                    if ''.join(sorted(other)) == sorted_string:
                        anagram_counter += 1
    return anagram_counter >= 153