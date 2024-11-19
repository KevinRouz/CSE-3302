# Kevin Farokhrouz
# 1002072886
# 11/18/2024
# Windows 11, Python 3.11.5



braces = [] # Stack to store braces
current_line = [] # List to store current line since we iterate through the file char by char
in_quote = False # Bool to store whether we are currently inside of a "quotation"
in_comment = False # Bool to store whether we are currently inside of a //Comment
in_multiline_comment = False # Bool to store whether we are currently inside of a /* multi line comment */

"""
    NOTE: There was a design decision made when separating in_comment and in_multiline_comment into two variables.
    It might not be strictly necessary to split it into two different variables this way, but I believe it makes the
    code a bit easier and explicit. It also helps me identify the proper nesting number to display when printing while
    inside of a multi line comment. Making this distinction is necessary to properly display this nesting number.
    
"""

filename = "input.txt"

with open(filename, "r") as file:
    content = file.read()
    prev_char = None
    for char in content:
        if char == "\n":
            
            """ 
                If the previous character was a closing brace then len(braces) will be one less then the actual nesting depth.
                This ensures that case will be handled properly.
                It also ensures that multi-line comments will display the proper nesting depth.
            """
            nesting_num = len(braces) if (prev_char != "}" or in_multiline_comment) else len(braces) + 1 
            
            print(f'{nesting_num} {"".join(current_line)}')
            current_line = []
            in_comment = False
            continue
        current_line.append(char)
        
        # If two consecutive // are found, this we are inside of a comment.
        if not in_comment and char == "/" and prev_char == "/":
            in_comment = True
        
        #If we find a quotation, we negate in_quote, which keeps track of whether we are in the quote or not.
        if char == '"' and not in_comment:
            in_quote = not in_quote
            
        if char == "*" and prev_char == "/":
            in_multiline_comment = True
        
        if char == "/" and prev_char == "*" and in_multiline_comment:
            in_multiline_comment = False
        
        # If we are in a comment or a quote, braces should be ignored and not handled.
        ignorebraces = in_comment or in_quote or in_multiline_comment
        
        # Handle braces if we are not ignoring braces
        if not ignorebraces:
            if char == "{":
                braces.append(char)
            elif char == "}":
                braces.pop()
        
        # Keep track of the previous character, needed for checking the beginning of a //Comment
        prev_char = char

# If braces is not empty, there are unmatched braces. return error.
if braces:
    raise InterruptedError("unmatched braces\n(expected '}', but found EOF.)")

# Print the last line, which is not printed inside of the loop since it's not ended by a \n newline.
print(f'{len(braces)} {"".join(current_line)}')