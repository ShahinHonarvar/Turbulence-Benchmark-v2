def palindrome_of_length_n(str):
    str = str.lower()
    result = set()
    for i in range(len(str) - 406):
        substr = str[i:i + 407]
        if substr == substr[::-1]:
            result.add(substr)
    return result