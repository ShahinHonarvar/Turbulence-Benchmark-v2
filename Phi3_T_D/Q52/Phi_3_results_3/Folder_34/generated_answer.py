def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s) - 32):
        substring = s[i:i + 33]
        if substring == substring[::-1]:
            results.add(substring)
    return results