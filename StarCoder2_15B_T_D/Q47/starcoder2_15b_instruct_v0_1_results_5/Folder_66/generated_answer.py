def palindromes_of_specific_lengths(text):
    substring = text[32:80]
    palindromes = set()
    for length in range(35, 42):
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