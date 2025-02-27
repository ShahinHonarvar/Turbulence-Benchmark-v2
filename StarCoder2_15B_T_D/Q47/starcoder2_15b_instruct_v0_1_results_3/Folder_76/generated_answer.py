def palindromes_of_specific_lengths(text):
    sub_text = text[101:293]
    palindromes = set()
    for length in range(154, 183):
        for start in range(len(sub_text) - length + 1):
            substring = sub_text[start:start + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes