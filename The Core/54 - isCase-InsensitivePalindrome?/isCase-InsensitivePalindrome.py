def isCaseInsensitivePalindrome(inputString):
    reverse = inputString[::-1]

    if inputString.lower() == reverse.lower():
        return True
    else:
        return False