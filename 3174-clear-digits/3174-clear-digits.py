class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []  # Initialize an empty stack to store non-digit characters

        for c in s:  # Iterate through each character in the input string
            if c.isdigit():  # Check if the character is a digit
                if stack:  # Ensure the stack is not empty before popping
                    stack.pop()  # Remove the last added character from the stack
            else:
                stack.append(c)  # If not a digit, add the character to the stack

        return ''.join(stack)  # Convert the stack list back to a string and return
