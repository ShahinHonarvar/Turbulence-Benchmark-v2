def palindrome_of_length_n(string):
    length = 97
    candidates = set()
    lower_string = string.lower()
    for i in range(len(lower_string) - length + 1):
        substring = lower_string[i:i + length]
        if substring.isalpha():
            if substring == substring[::-1]:
                candidates.add(substring)
    return candidates