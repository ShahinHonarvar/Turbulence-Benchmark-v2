def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 604 <= i < 949 and 'N' < char <= 'U' and (char in vowels)]
    return result