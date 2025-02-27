def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[23:78]
    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                window_letters = [c for c in window if c.isalpha()]
                if len(window_letters) == length:
                    palindromes.add(window.lower())
    return palindromes