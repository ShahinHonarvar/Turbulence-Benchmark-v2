def palindromes_between_indices(string):
    string = string.lower()
    s = set()
    for i in range(len(string) - 7):
        for j in range(i + 4, len(string) - 3):
            if string[i:j + 1] == string[i:j + 1][::-1]:
                s.add(string[i:j + 1])
    return s