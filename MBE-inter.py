import sys

class MBPInterpreter:
    def __init__(self):
        self.variables = {}
        self.running = False

    def interpret(self, code):
        lines = code.split("\n")
        line_number = 0
        for line in lines:
            line_number += 1
            line = line.strip()
            if line.startswith("Please "):
                tokens = line.split(" ")
                command = tokens[1]
                if len(tokens) > 2:
                    content = " ".join(tokens[2:])
                    if command == "Screen":
                        print(content[1:-1])  # Remove quotes from the content
                    elif command == "Input":
                        var_name = tokens[2]
                        user_input = input(f"Please enter a value for {var_name}: ")
                        self.variables[var_name] = user_input
                    elif command == "Die.":
                        self.running = False
                        break
                    else:
                        print(f"Sorry, MBP doesn't understand the command on line {line_number}.")
                        self.running = False
                        break
                else:
                    print(f"Sorry, MBP requests additional content after commands on line {line_number}.")
                    self.running = False
                    break
            elif line.strip() == "":
                continue  # Skip empty lines
            else:
                print(f"Sorry, MBP requests all lines to begin with 'Please' on line {line_number}.")
                self.running = False
                break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mbp_interpreter.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            interpreter = MBPInterpreter()
            code = file.read()
            interpreter.running = True
            interpreter.interpret(code)
    except FileNotFoundError:
        print("File not found. Please provide a valid file.")
