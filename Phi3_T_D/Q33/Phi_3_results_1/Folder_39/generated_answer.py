def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [chr(i) for i in range(128) if 32 <= i < 97 and i > ord('q') and (i <= ord(']')) and (chr(i) in vowels)]
    return result