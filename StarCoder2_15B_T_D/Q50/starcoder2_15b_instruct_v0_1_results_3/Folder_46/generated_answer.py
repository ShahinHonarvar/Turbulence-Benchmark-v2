from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter(strings)
    for string in strings:
        for other_string in strings:
            if string != other_string and sorted(string.lower()) == sorted(other_string.lower()) and (len(string) >= 3):
                counter[string] -= 1
                counter[other_string] -= 1
                if counter[string] == 0 and counter[other_string] == 0:
                    return True
    return False