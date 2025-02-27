import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string).lower()
    palindromes = [string[i:i + 119] for i in range(len(string) - 118) if string[i:i + 119] == string[i:i + 119][::-1]]
    return set(palindromes)