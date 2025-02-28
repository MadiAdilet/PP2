import re 

def ab(s):
    if re.fullmatch(r'^ab*$', s):
        return True
    else:
        return False


text = ["a", "ab", "abb", "ac", "b", "abc", "aab"]
for i in range(len(text)):
    print(text[i],ab(text[i]))
