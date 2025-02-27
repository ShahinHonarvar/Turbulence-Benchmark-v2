def palindrome_of_length_at_least_n(s):
    n = 45
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(n, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub_str = s[i:i + length]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes