def palindromes_of_specific_lengths(string):
    substring = string[15:96]
    palindromes = set()
    for i in range(len(substring) - 19):
        for length in range(20, 67):
            if i + length - 1 >= len(substring):
                continue
            substring_to_check = substring[i:i + length]
            if substring_to_check.lower() == substring_to_check[::-1].lower():
                palindromes.add(substring_to_check)
    return palindromes