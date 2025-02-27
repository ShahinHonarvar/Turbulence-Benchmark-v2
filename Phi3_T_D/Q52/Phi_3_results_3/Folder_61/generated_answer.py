def palindrome_of_length_n(s):
    length = 74
    s = s.lower()
    palindromes_set = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring[:length // 2].lower() == substring[length // 2:][::-1].strip():
            palindromes_set.add(substring)
    return palindromes_set