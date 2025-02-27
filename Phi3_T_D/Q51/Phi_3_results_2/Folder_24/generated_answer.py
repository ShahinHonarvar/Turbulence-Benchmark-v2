from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    sorted_strings = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    sorted_len = len(sorted_strings)
    for i in range(sorted_len):
        for j in range(i + 1, sorted_len):
            if sorted_strings[i] == sorted_strings[j]:
                count += 1
                if count > 96:
                    return False
    return True