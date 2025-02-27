def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[43:96]
    for i in range(len(substring) - 17):
        for j in range(18, 48):
            if i + j - 1 < len(substring):
                window = substring[i:i + j]
                if window.lower() == window[::-1].lower():
                    palindromes.add(window)
    return palindromes