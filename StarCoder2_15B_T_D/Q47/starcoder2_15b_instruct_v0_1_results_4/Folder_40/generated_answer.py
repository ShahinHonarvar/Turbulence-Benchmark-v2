def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[:6]
    palindromes = set()
    for length in range(3, 6):
        for i in range(len(substring) - length + 1):
            substring_to_check = substring[i:i + length]
            if substring_to_check == substring_to_check[::-1]:
                palindromes.add(substring_to_check)
    return palindromes