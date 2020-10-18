
print("Welcome to the Python Calculator exercise program.")

def calculate(par1, op, par2):
    if (op == 'x'):
        return par1 * par2
    elif op == '+':
        return par1 + par2
    elif op == '-':
        return par1 - par2
    elif op == '/':
        return par1 // par2
    elif op == '%':
        return par1 % par2
    elif op == '^':
        return par1 ** par2

 
with open("step4.txt", "r") as f:
    list_of_calculations = f.readlines()

index = 1
processed_indices  = []
print("There are {0} lines in this file.".format(len(list_of_calculations)))

not_revisiting = True
while index in range(1, len(list_of_calculations)) and not_revisiting:
    print("\r\nStep {0}:".format(len(processed_indices )))
    # get the line in the list (we have to take off 1 because line numbers in the list don't start at 0) 
    line= list_of_calculations[index-1]
    line = line.strip() 
    if (index in processed_indices ):
        not_revisiting = False
        print("We have seen line number {0} before {1} so exiting the program".format(index, line))
        break
    
    values = line.split()

    print(line)
    if (values[1] == "calc"):
        param1int = int(values[3])
        param2int = int(values[4])    
        new_line_number = calculate(param1int, values[2], param2int)
            
    elif (values[0] == "goto"):
        new_line_number = int(values[1])
    elif (values[0] == "remove"):
        new_line_number = int(values[1])
        line_to_remove = list_of_calculations[new_line_number-1]       
        print("Removing line {0} which is {1}".format(new_line_number, line_to_remove.strip()))
        if (0 <= new_line_number-1 < len(list_of_calculations)-1):
            list_of_calculations.remove(line_to_remove)
        new_line_number = index + 1
    elif (values[0] == "replace"):
        line_number_to_be_replaced = int(values[1])
        line_number_to_replace = int(values[2])
        print("Replacing line {0} with line {1}".format(line_number_to_be_replaced, line_number_to_replace ))
        if ((0 <= (line_number_to_be_replaced - 1) < len(list_of_calculations)-1) and (0 <= (line_number_to_replace - 1) < len(list_of_calculations)-1)):
            line_to_replace = list_of_calculations[line_number_to_replace-1]
            list_of_calculations[line_number_to_be_replaced-1] = line_to_replace
        new_line_number = index+1
    else:
        print("Got unexpected value: {0}".format(values[1]))

    processed_indices.append(index)
    print("Added {0} to the processes indices list".format(index))
    print("Setting new index to {0}".format(new_line_number))
    
    index = new_line_number 

print("Processed {0} lines".format(processed_indices)) 
if (not_revisiting):
    print("Went outside the range")
else:
    print("Found duplicate line {0} at line number {1}".format(list_of_calculations[index-1], index))




    

        



