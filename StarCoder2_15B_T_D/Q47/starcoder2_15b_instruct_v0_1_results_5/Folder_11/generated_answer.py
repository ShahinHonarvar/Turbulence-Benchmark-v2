def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[24:98]
    for length in range(10, 37):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindrome = window.lower()
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes