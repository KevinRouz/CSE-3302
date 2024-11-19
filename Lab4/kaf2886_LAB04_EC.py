# Kevin Farokhrouz
# 1002072886
# 11/18/2024
# Windows 11, Python 3.11.5

"""
    NOTE: Submitting for Extra credit A and B.
"""

braces = [] # Stack to store braces
current_line = [] # List to store current line since we iterate through the file char by char
in_quote = False # Bool to store whether we are currently inside of a "quotation"
in_comment = False # Bool to store whether we are currently inside of a //Comment
in_multiline_comment = False # Bool to store whether we are currently inside of a /* multi line comment */


# Helper function to print the current line
def printline(current_line):
    """ 
        If the previous character was a closing brace then len(braces) will be one less then the actual nesting depth.
        This ensures that case will be handled properly.
        It also ensures that comments will display the proper nesting depth.
    """
    nesting_num = len(braces) if (prev_char != "}" or in_multiline_comment or in_comment) else len(braces) + 1     
    tabs = "    " * nesting_num    
    if current_line:
        print(f'{nesting_num} {tabs}{"".join(current_line)}')
    
    # Returns nesting_num if needed.
    return nesting_num

"""
    NOTE: There was a design decision made when separating in_comment and in_multiline_comment into two variables.
    It might not be strictly necessary to split it into two different variables this way, but I believe it makes the
    code a bit easier and explicit. It also helps me identify the proper nesting number to display when printing while
    inside of a multi line comment. Making this distinction is necessary to properly display this nesting number.
    
"""

filename = "input_EC.txt"

with open(filename, "r") as file:
    content = file.read()
    prev_char = None
    for char in content:
        if char == "\n" or char == ";":
            if char == ";":
                current_line.append(";")
            printline(current_line)
            current_line = []
            in_comment = False
            continue
        # Skip all leading spaces (tabs). Tabs will be handled based on the nesting depth.
        if not current_line and char == " ":
            continue
        
        # Append char if it's not a brace, those will be handled separately.
        if not char == "{" and not char == "}":
            current_line.append(char)
        
        # If two consecutive // are found, this we are inside of a comment.
        if not in_comment and char == "/" and prev_char == "/":
            in_comment = True
        
        #If we find a quotation, we negate in_quote, which keeps track of whether we are in the quote or not. Handles the case where it can be escaped using the escape operator \
        if char == '"' and not prev_char == "\\":
            in_quote = not in_quote
            
        # Handle multi-line comments.
        if char == "*" and prev_char == "/":
            in_multiline_comment = True
        
        if char == "/" and prev_char == "*" and in_multiline_comment:
            in_multiline_comment = False
        
        # If we are in a comment or a quote, braces should be ignored and not handled.
        ignorebraces = in_comment or in_quote or in_multiline_comment
        
        # Handle braces if we are not ignoring braces. Print the current line, then the corresponding brace.
        if not ignorebraces:
            if char == "{":
                nestingnum = printline(current_line)
                current_line = []
                braces.append(char)
                tabs = "    " * nestingnum   
                print(f'{nestingnum + 1} {tabs}{char}')
            elif char == "}":
                printline(current_line)
                current_line = []
                braces.pop()
                tabs = "    " * len(braces)
                print(f'{len(braces)+1} {tabs}{char}')
                
        #If not ignoring braces, we can append them to the current_line.
        else:
            if char == "{" or char == "}":
                current_line.append(char)
        
        # Keep track of the previous character, needed for checking the beginning of a //Comment
        prev_char = char

# If braces is not empty, there are unmatched braces. return error.
if braces:
    raise InterruptedError("unmatched braces\n(expected '}', but found EOF.)")

# Print the last line if it was not already printed.
if current_line:
    printline(current_line)