def count_anagrams(string, charset):
    count_dict = {}
    for char in string:
        if char in charset:
            count_dict[char.lower()] = count_dict.get(char.lower(), 0) + 1
    return count_dict

def is_anagram(str1, str2):
    return count_anagrams(str1, 'abcdefghijklmnopqrstuvwxyz') == count_anagrams(str2, 'abcdefghijklmnopqrstuvwxyz')

def if_contains_anagrams(string_list):
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3 and is_anagram(string_list[i], string_list[j]):
                anagram_count += 1
    return anagram_count <= 92