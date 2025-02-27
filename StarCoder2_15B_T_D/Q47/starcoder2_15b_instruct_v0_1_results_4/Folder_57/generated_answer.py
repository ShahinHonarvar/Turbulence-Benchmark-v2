def palindromes_of_specific_lengths(s):
    substring = s[16:95].lower()
    palindromes = set()
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1] and window.isalpha():
                palindromes.add(window)
    return palindromes