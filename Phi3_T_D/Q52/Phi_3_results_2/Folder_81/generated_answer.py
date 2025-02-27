def palindrome_of_length_n(s):
    results = set()
    s_lower = s.lower()
    for i in range(len(s) - 89):
        substring = s_lower[i:i + 99]
        if substring.isalpha() and substring == substring[::-1]:
            results.add(substring)
    return results