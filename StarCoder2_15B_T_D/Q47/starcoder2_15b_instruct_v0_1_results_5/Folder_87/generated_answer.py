def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[11:94]
    for length in range(34, 55):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes