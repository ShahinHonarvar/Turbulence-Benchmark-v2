def palindrome_of_length_n(string):
    substrings = set()
    for i in range(len(string) - 89):
        substring = string[i:i + 90]
        if substring == substring[::-1]:
            substrings.add(substring)
    return substrings