
print("Welcome to the Python Calculator exercise program.")
# print("I will ask you for your operator, it must be one of x, +, -, / or -1 to exit")
# operator = input("Please enter your operator: ")

def valid_operator(op):
    times = op == 'x'
    add = op == '+'
    division = op == '/'
    minus = op == '-'
    
    return (times or add or division or minus)

def calculate(par1, op, par2):
    if (op == 'x'):
        return par1 * par2
    elif op == '+':
        return par1 + par2
    elif op == '-':
        return par1 - par2
    elif op == '/':
        return par1 // par2
    elif op =='^':
        return par1 ** par2
 
with open("step3.txt", "r") as f:
    list_of_calculations = f.readlines()

result = 0

index = 0
length = len(list_of_calculations)-1
processed_lines = {}
processed_lines_counter = 0
print("There are {0} lines in this file.".format(length))

not_revisiting = True
while index in range(0, length) and not_revisiting:
    
    
    line = list_of_calculations[index]
    if (index in processed_lines):
        not_revisiting = False
        print("We have seen this line before {0} {1} so exiting the program".format(index, line))
        break
    
    print ("Reading line {0}".format(line))
    values = line.split()
    print ("Values are {0}".format(values))

    if (values[1] == "calc"):
        param1int = int(values[3])
        param2int = int(values[4])
        
        print("Calculating...")
        loc = calculate(param1int, values[2], param2int)
        print(" ... result {0}".format(loc))
        
    elif (values[0] == "goto"):
        loc = int(values[1])
        print("Goto {0}".format(loc))
    elif (values[0] == "remove"):
        loc = int(values[1])
        print("Removing {0}".format(loc))
        line_to_remove = list_of_calculations[loc]
    elif (values[0] == "replace"):

    else:
        print("Got unexpected value: {0}".format(values[1]))

    processed_lines[processed_lines_counter] = index
    processed_lines_counter += 1
    print("Setting new index to {0}".format(loc))
    index = loc
    

    
        
  
    

print ("Result is {0}".format(result))




    

        



