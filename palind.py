def palind(s):
    rev = ""
    for i in s:
        rev = i + rev
    if rev == s:
        return True
    return False
print(palind("madammimadam"))
print(palind("madaminadam"))
print(palind("ratsliveonnoevilstar"))
print(palind("amanapanacanalpanama"))