def palindromes_of_specific_lengths(string):
    palindromes = set()
    lower_string = string.lower()
    length_range = range(13, 43)
    substring = lower_string[44:100]
    for length in length_range:
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes