def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i + 86, len(string) + 1):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result