def htmlEndTagByStartTag(startTag):
    tag = ""
    
    for i in startTag:
        if i not in (' ', '>'):
            tag += i
        else:
            break
        
    tag = list(tag)
    tag.insert(1, "/")
    tag.append(">")
    
    return "".join(tag)