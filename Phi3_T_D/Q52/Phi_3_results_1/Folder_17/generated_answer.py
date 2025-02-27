def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 288):
        substring = s[i:i + 289]
        if substring == substring[::-1]:
            result.add(substring.capitalize())
    return result