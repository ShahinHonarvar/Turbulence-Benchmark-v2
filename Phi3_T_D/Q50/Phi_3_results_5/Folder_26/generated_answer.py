def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    filtered_list = [s for s in lst if len(s) >= 3]
    count = 0
    for i in range(len(filtered_list)):
        for j in range(i + 1, len(filtered_list)):
            if is_anagram(filtered_list[i], filtered_list[j]):
                count += 1
                if count >= 49:
                    return True
    return False