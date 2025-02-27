def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[15:96]
    for length in range(20, 67):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindrome = ''
                for char in window:
                    if char.isalpha():
                        palindrome += char
                if len(palindrome) == length:
                    palindromes.add(palindrome.lower())
    return palindromes