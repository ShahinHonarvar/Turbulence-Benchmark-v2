def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for index, char in enumerate(s) if 13 <= index < 35 and '8' < char <= 'F' and (char in vowels)]
    return result