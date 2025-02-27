def palindromes_of_specific_lengths(string):
    sub_string = string[26:91]
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(sub_string) - length + 1):
            substring = sub_string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes