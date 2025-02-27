def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[28:95]
    for i in range(len(substring) - 38):
        for length in range(38, 50):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindrome = window.lower()
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes