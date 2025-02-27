def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string) - 40):
        for j in range(i + 40, len(string)):
            if string[i:j + 1] == string[i:j + 1][::-1] and all((c.isalpha() for c in string[i:j + 1])):
                result.add(string[i:j + 1])
    return result