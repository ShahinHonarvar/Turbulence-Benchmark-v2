from itertools import product

def palindromes_of_specific_lengths(s):
    selected_substring = s[23:83]
    lower_bound = 32
    upper_bound = 34
    palindromes = set()
    for length in range(lower_bound, upper_bound + 1):
        for start_pos in range(0, len(selected_substring) - length + 1):
            substring = selected_substring[start_pos:start_pos + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes