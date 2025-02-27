def palindromes_of_specific_lengths(string):
    palindromes = set()
    sub_string = string[200:301]
    for length in range(10, 51):
        for start in range(len(sub_string) - length + 1):
            substring = sub_string[start:start + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes