import re

def abb(s):
    if re.fullmatch(r'a[b]{2,3}',s):
        return True
    else:
        return False
print(abb("abb"))
print(abb("abbb"))
print(abb("ab"))