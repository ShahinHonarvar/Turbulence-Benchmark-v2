def palindromes_of_specific_lengths(s):
    substring = s[13:96]
    palindromes = set()
    for length in range(57, 61):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes