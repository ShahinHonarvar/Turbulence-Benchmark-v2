def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[124:284]
    for length in range(115, 135):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes