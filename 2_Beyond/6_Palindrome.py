show_expected_result = False
show_hints = False

def is_Palindrome(str):
    temp = str.lower()
    newstr = ""
    for c in temp:
        if c.isalnum():
            newstr += c
        
    reverseStr=""
    strindx = len(newstr)-1
    while (strindx >= 0):
        reverseStr += newstr[strindx]
        strindx -= 1
    
    if newstr == reverseStr:
        return True
    return False

test_word = "RACE CAR"
result = is_Palindrome(test_word)
print('Is '+test_word+' a Palindrome ?', result)