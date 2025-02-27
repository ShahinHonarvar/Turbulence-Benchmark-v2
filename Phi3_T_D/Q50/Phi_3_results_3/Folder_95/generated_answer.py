def if_contains_anagrams(string_list):
    sorted_list = [''.join(sorted(word.lower())) for word in string_list if len(word) >= 3]
    anagram_count = 0
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i] == sorted_list[j]:
                anagram_count += 1
                if anagram_count >= 93:
                    return True
    return False