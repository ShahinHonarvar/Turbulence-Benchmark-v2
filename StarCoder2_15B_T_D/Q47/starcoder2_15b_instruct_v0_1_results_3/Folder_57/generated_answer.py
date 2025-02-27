def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[16:95]
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            substring_to_check = substring[i:i + length]
            if substring_to_check.lower() == substring_to_check[::-1].lower():
                if all((c.isalpha() for c in substring_to_check)):
                    palindromes.add(substring_to_check)
    return palindromes