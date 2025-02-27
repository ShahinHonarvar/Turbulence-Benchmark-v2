def palindromes_of_specific_lengths(s):
    substr = s[:101]
    upper = substr.upper()
    palindromes = {substr[i:j + 1] for i in range(len(substr)) for j in range(i, min(i + 15, len(substr))) if i < j and substr[i:j + 1].isalpha() and (substr[i:j + 1] == substr[i:j + 1][::-1]) and (3 <= len(substr[i:j + 1]) <= 15)}
    lowercase_palindromes = {substr[i:j + 1].lower() for i in range(len(substr)) for j in range(i, min(i + 15, len(substr))) if i < j and substr[i:j + 1].isalpha() and (substr[i:j + 1] == substr[i:j + 1][::-1]) and (3 <= len(substr[i:j + 1]) <= 15)}
    return lowercase_palindromes