def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 42):
        for j in range(i + 43, length + 1):
            sub_str = s[i:j]
            if sub_str.isalpha() and sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes