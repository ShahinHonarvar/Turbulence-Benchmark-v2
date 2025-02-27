def palindrome_of_length_n(input_string):
    s = input_string.lower()
    n = len(s)
    result = set()
    for i in range(n):
        if i + 16 < n:
            substring = s[i:i + 17]
            if substring == substring[::-1]:
                result.add(substring)
    return result