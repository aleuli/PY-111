def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    list_brackets = []
    flag_ = True
    open_ = "({["
    close_ = ")}]"

    for i in brackets_row:
        if i in open_:
            list_brackets.append(i)
            continue
        elif i in close_:
            if len(list_brackets) >= 1:
                list_brackets.pop()
            else:
                flag_ = False
    if flag_ is True and len(list_brackets) == 0:
        return True
    else:
        return False
