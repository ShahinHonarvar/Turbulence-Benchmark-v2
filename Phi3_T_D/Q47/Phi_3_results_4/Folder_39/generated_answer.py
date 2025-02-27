def palindromes_of_specific_lengths(input_string):
    substr = input_string[31:92].lower()
    palindromes = set()
    for center in range(35, 58):
        expand_arm = 2
        while center - expand_arm >= 0 and center + expand_arm < len(substr):
            if substr[center - expand_arm].isalpha() and substr[center + expand_arm].isalpha():
                if substr[center - expand_arm] == substr[center + expand_arm]:
                    palindrome_length = expand_arm * 2 + 1
                    palindromes.add(substr[center - expand_arm:center + expand_arm + 1])
                    expand_arm += 1
                else:
                    break
            else:
                break
    return palindromes