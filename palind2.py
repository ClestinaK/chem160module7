def palind2(s):
    alist = list(s)
    alist.reverse()
    rev = "".join(alist)
    if rev == s:
        return True
    return False
print(palind2("ratsliveonnoevilstar"))
print(palind2("abcdedcba"))