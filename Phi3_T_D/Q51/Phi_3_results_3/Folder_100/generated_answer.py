def if_contains_anagrams(word_list):
    counted = {}
    for word in word_list:
        word = word.lower()
        if len(word) >= 3:
            key = ''.join(sorted(word))
            if key in counted:
                counted[key] += 1
            else:
                counted[key] = 1
    anagram_pairs = sum((count // 2 for count in counted.values()))
    return anagram_pairs <= 98