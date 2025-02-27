def palindrome_of_length_n(s):
    substrings = set()
    for i in range(len(s) - 89):
        for j in range(i + 90, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindrome = ''
                for char in substring:
                    if char.isalpha():
                        palindrome += char
                if len(palindrome) == 90:
                    substrings.add(palindrome)
    return substrings