from collections import defaultdict

def all_substrings(s):
    length = len(s)
    return {s[i:j] for i in range(length) for j in range(i + 1, length + 1)}

def extend_palindromes(string, length, palindromes):
    for i in range(len(string) - length + 1):
        if string[i].isalpha() and string[i - 1:i + length + 1].lower() == string[i - 1:i + length + 1][::-1].lower():
            palindromes.add(string[i:i + length])
    return palindromes

def palindrome_of_length_n(input_string):
    half_length = 279 // 2
    palindromes = set()
    extensions_queue = [(input_string, half_length)]
    while extensions_queue:
        string, length = extensions_queue.pop(0)
        substring_set = all_substrings(string)
        if length == 1:
            for sub in substring_set:
                if sub.isalpha():
                    palindromes.add(sub)
        else:
            for sub in substring_set:
                if len(sub) < length:
                    continue
                if sub.lower() == sub[::-1].lower():
                    palindromes.add(sub)
                if sub.isalpha():
                    extensions_queue.append((sub, length - 1))
    return palindromes