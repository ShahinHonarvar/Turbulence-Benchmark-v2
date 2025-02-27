def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[18:99]
    for length in range(31, 52):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window == window[::-1]:
                palindrome = window.lower()
                if all((ch.isalpha() for ch in palindrome)):
                    palindromes.add(palindrome)
    return palindromes