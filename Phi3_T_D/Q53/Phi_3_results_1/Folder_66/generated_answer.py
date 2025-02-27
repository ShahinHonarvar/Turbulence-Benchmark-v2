def palindrome_of_length_at_least_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s) - 75):
        for j in range(i + 76, len(s) + 1):
            if all((c.isalpha() for c in s[i:j])):
                palindrome_sliced = s[i:j]
                if palindrome_sliced == palindrome_sliced[::-1]:
                    results.add(palindrome_sliced)
    return results