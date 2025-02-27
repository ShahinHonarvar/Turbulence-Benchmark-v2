def palindromes_of_specific_lengths(string):
    sub_string = string[36:93]
    palindromes = set()
    for length in range(10, 36):
        for i in range(len(sub_string) - length + 1):
            substring = sub_string[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes