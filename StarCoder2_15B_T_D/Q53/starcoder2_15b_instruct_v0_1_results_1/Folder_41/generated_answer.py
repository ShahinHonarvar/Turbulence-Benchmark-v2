def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i].isalpha() and string[j].isalpha() and (string[i].lower() == string[j].lower()):
                palindrome = string[i].lower() + string[j].lower()
                k = 1
                while i - k >= 0 and j + k < len(string) and (string[i - k].lower() == string[j + k].lower()):
                    palindrome = string[i - k].lower() + palindrome + string[j + k].lower()
                    k += 1
                if len(palindrome) >= 28:
                    palindromes.add(palindrome)
    return palindromes