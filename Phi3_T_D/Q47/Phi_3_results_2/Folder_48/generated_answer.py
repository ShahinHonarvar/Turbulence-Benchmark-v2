def palindromes_of_specific_lengths(input_string):
    substring = input_string[155:284]
    palindromes = {substring[i:i + length] for length in range(104, 121) for i in range(len(substring) - length + 1) if substring[i:i + length].isalpha() and substring[i:i + length].lower() == substring[i:i + length][::-1]}
    return palindromes