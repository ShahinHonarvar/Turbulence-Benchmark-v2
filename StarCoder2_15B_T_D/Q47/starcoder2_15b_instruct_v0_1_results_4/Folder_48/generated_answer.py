def palindromes_of_specific_lengths(text):
    sub_string = text[155:284]
    palindromes = set()
    for length in range(104, 121):
        for i in range(len(sub_string) - length + 1):
            substring = sub_string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes