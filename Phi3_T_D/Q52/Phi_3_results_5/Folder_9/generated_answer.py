def palindrome_of_length_n(string):
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 71):
        if all((c in valid_chars for c in string[i:i + 72])):
            if string[i:i + 72] == string[i:i + 72][::-1]:
                palindromes.add(string[i:i + 72].upper())
    return palindromes