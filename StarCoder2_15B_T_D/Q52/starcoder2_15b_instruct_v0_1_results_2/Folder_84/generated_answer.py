def palindrome_of_length_n(string):
    if len(string) < 131:
        return set()
    palindromes = set()
    for i in range(len(string) - 131 + 1):
        substring = string[i:i + 131]
        if substring == substring[::-1]:
            is_palindrome = True
            for c in substring:
                if not c.isalpha():
                    is_palindrome = False
                    break
            if is_palindrome:
                palindromes.add(substring)
    return palindromes