def palindrome_of_length_n(s):
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 54, len(s) + 1) if s[i:j].isalpha() and len(s[i:j]) == 54 and (s[i:j].lower() == s[i:j][::-1].lower())}
    return palindromes