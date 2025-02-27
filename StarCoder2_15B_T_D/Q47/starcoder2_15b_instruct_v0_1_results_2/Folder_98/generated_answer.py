def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[0:21]
    for length in range(5, 81):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                if window.isalpha():
                    palindromes.add(window)
    return palindromes