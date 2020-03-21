def isUnstablePair(filename1, filename2):
    if (filename1 > filename2 and filename1.lower() > filename2.lower()) \
    or (filename1 < filename2 and filename1.lower() < filename2.lower()):
        return False
    
    return True