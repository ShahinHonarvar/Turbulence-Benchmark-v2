def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 19 <= i < 32 and '0' < char <= '7' and (char in vowels)]
    return result