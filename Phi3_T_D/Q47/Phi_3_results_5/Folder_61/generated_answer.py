def palindromes_of_specific_lengths(input_string):
    substring = input_string[:31].lower()
    palindromes = {substring[i:i + l] for l in range(20, 31) for i in range(len(substring) - l + 1) if substring[i:i + l].isalpha() and substring[i:i + l] == substring[i:i + l][::-1]}
    return palindromes