def palindrome(string):
    if string == string[::-1]:
        return True
    return False
c = palindrome('abca')
print(c)

