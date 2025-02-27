def palindromes_of_specific_lengths(input_string):
    start, end = (26, 84)
    palindromes = set()
    for length in range(30, 47):
        for i in range(start, end - length + 1):
            substring = input_string[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes