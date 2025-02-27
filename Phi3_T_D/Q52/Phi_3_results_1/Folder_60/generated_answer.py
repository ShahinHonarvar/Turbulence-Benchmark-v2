def palindrome_of_length_n(string):
    result = set()
    string = string.lower()
    for i in range(len(string) - 87):
        substr = string[i:i + 88]
        if substr == substr[::-1]:
            result.add(substr)
    return result