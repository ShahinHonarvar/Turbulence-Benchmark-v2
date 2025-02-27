from itertools import combinations

def palindromes_of_specific_lengths(s):
    s = s[10:97]
    palindromes = set()
    for length in range(45, 53):
        for start_index in range(len(s) - length + 1):
            substring = s[start_index:start_index + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes