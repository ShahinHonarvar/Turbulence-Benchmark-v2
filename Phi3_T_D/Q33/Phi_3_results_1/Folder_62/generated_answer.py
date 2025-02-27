def return_vowels(s):
    vowels = ['E', 'I', 'O', 'U']
    start, end = (14, 60)
    result = [char for char in s[start:end] if char in vowels and ord(char) > ord('E')]
    return result