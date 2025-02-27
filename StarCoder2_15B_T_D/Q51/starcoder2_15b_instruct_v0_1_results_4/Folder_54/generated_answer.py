def if_contains_anagrams(strings):
    anagrams = []
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagrams.append((strings[i], strings[j]))
    return len(anagrams) <= 39

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if str1.count(letter) != str2.count(letter):
            return False
    return True