def return_vowels(s):
    result = [ch for ch in s[464:574] if ch in 'ehioyueaieou']
    return [ch for ch in result if 'a' < ch <= 'g']