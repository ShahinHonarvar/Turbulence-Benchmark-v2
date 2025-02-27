def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for i, char in enumerate(s) if 32 <= i < 97 and char > 'Q' and (char <= ']') and (char in vowels)]
    return result