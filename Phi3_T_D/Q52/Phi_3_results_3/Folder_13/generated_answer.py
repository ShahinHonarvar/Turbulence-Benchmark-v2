def palindrome_of_length_n(s):
    candidates = set(s.lower())
    candidates = {ch for ch in candidates if ch.isalpha()}
    palindromes = set()
    length = 206
    for i in range(len(s) - length + 1):
        substring = s[i:i + length].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes