def palindrome_of_length_n(s):
    s = s.lower()
    subsets = set()
    length = 257
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            subsets.add(substring)
    return subsets if subsets else set()