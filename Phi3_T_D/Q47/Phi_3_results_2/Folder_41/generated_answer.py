from itertools import combinations

def palindromes_of_specific_lengths(s):
    substr = s[1:8]
    valid_substr = ''.join(filter(str.isalpha, substr))
    result_set = set()
    for length in range(3, 5):
        for i in range(len(valid_substr) - length + 1):
            substring = valid_substr[i:i + length]
            if substring.lower() == substring[::-1].lower():
                result_set.add(substring.lower())
    return result_set