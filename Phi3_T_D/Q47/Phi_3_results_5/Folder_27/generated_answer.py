def palindromes_of_specific_lengths(s):
    starting_index = 13
    ending_index = 99
    palindromes = set()
    for length in range(26, 30):
        for i in range(starting_index, ending_index - length + 2):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes