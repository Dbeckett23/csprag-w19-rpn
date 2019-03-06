stack = []

def add():
    stack.append(stack.pop() + stack.pop())

def subtract():
    stack.append(stack.pop() - stack.pop())

def handleInput(input):
    if(input.isnumeric()):
        stack.append(int(input))
    else:
        # its a string, i.e +,-,*,/ or junk
        if(len(stack) < 2):
            return
        if(input == '+'):
            add()
        elif(input == '-'):
            subtract()


def calculate(arg):
    input = arg.split()
    for x in range(len(input)):
        handleInput(input[x])
    if(len(stack) == 0):
        return 0
    else :
        return stack[len(stack)-1]
            
def main():
    while True: 
        calculate(input("rpn calc> "))

if __name__=='__main__':
    main()
