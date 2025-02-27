def palindromes_of_specific_lengths(string):
    substring = string[27:96]
    palindromes = set()
    for length in range(49, 52):
        for i in range(len(substring) - length + 1):
            substring_to_check = substring[i:i + length]
            if substring_to_check.lower() == substring_to_check[::-1].lower():
                if all((char.isalpha() for char in substring_to_check)):
                    palindromes.add(substring_to_check)
    return palindromes