def palindromes_of_specific_lengths(string):
    substring = string[16:78]
    palindromes = set()
    for length in range(43, 48):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindrome = ''
                for char in window:
                    if char.isalpha():
                        palindrome += char
                if len(palindrome) == length:
                    palindromes.add(palindrome)
    return palindromes