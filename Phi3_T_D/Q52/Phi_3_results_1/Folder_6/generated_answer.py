def palindrome_of_length_n(s):
    filtered_s = ''.join((c for c in s.lower() if c.isalpha()))
    palindromes = set(filter(lambda p: p.lower() == p.lower()[::-1], [filtered_s[i:i + 474] for i in range(len(filtered_s) - 473)]))
    return palindromes