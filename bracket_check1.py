from Stack import Stack

def bracket_check(test_string):
    stack = Stack()
    opening_brackets = "({["
    closing_brackets = ")}]"

    is_error = False
    location = []

    for i in range(len(test_string)):
        char = test_string[i]

        if char in opening_brackets:
            stack.push((char, i))

        elif char in closing_brackets:
            if stack.isEmpty():
                is_error = True
                location.append(i)
            else:
                top, idx = stack.pop()
                if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                    is_error = True
                    location.append(i)
                    break

    if not stack.isEmpty():
        is_error = True
        while not stack.isEmpty():
            top, idx = stack.pop()
            location.append(idx)

    return is_error, location
test_string = '{}{'
isError, locations = bracket_check(test_string)
print(f'error: {isError}')
print('location:', locations)