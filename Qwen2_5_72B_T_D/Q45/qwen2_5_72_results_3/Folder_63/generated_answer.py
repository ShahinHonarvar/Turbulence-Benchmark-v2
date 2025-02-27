from collections import Counter

def palindromes_between_indices(s):
    substring = s[0:4]
    counter = Counter(filter(str.isalpha, substring.lower()))
    result = set()
    for length in range(3, 4):
        for char, count in counter.items():
            if count >= 2:
                if length == 3:
                    for center in counter.keys():
                        if center != char or count > 2:
                            result.add(char + center + char)
                else:
                    result.add(char * 4)
    return result