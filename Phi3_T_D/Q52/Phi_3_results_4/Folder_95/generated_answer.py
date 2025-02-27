def palindrome_of_length_n(s):
    unique_palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 87, len(s) + 1):
            substring = s[i:j]
            if len(substring) != 87:
                break
            if substring == substring[::-1]:
                unique_palindromes.add(substring)
    return unique_palindromes