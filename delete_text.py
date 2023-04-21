def delete(text):
    i = 0
    count_opened = 0
    if_closed = False
    while i < len(text):
        if text[i] == '(':
            count_opened += 1
            text = text[:i] + text[i + 1:]
        if text[i] == ')':
            count_opened -= 1
            text = text[:i] + text[i + 1:]
            if_closed = True
        if count_opened > 0:
            if not if_closed:
                text = text[:i] + text[i + 1:]
            if_closed = False
        else:
            if i != len(text) and text[i] != '(':
                i += 1
    return text

