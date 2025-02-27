def if_contains_anagrams(lst):
    n = len(lst)
    anagram_dict = {}
    for i in range(n):
        sorted_word = ''.join(sorted(lst[i].lower()))
        if len(lst[i]) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(i)
            else:
                anagram_dict[sorted_word] = [i]
    anagram_pairs = 0
    for key, value in anagram_dict.items():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs <= 206