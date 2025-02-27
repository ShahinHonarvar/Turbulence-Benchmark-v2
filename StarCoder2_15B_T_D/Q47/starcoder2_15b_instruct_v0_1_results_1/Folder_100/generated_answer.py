def palindromes_of_specific_lengths(text):
    sub_string = text[29:97]
    palindromes = set()
    for length in range(12, 19):
        for start in range(len(sub_string) - length + 1):
            window = sub_string[start:start + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes