def palindromes_of_specific_lengths(string):
    substring = string[32:80]
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            substring_to_check = substring[i:i + length]
            if substring_to_check.lower() == substring_to_check[::-1].lower():
                palindromes.add(substring_to_check)
    return list(palindromes)