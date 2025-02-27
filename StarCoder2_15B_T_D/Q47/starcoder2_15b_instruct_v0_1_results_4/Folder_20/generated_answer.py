def palindromes_of_specific_lengths(string):
    substring = string[20:75]
    palindromes = set()
    for length in range(36, 43):
        for start in range(len(substring) - length + 1):
            substring_to_check = substring[start:start + length]
            if substring_to_check.lower() == substring_to_check[::-1].lower():
                palindromes.add(substring_to_check)
    return palindromes