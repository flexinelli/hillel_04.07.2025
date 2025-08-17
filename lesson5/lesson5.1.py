test_string = input("Enter name of variable: ")
allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789_"
keywords = ["False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del",
            "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda",
            "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]

if len(test_string) == 0:
    print("False")
else:
    for ch in test_string:
        if ch not in allowed_chars:
            print("False")
            break
    else:
        if test_string[0].isdigit():
            print("False")
        else:
            if "__" in test_string:
                print("False")
            elif test_string in keywords:
                print("False")
            else:
                print("True")