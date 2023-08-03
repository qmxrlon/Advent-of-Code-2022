from string import ascii_uppercase

# Getting input
with open('day5.in') as file:
    stack_strings, instructions = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))


stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ","")}
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]

def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")


def loadStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] == " ":
                pass
            else:
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

def getStackEnds():
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer

loadStacks()
for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]

    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    for crate in range(crates):
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)

print("Answer to part 1: ", getStackEnds())


emptyStacks()
loadStacks()
for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]

    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    crates_to_remove = stacks[from_stack][-crates:]
    stacks[from_stack] = stacks[from_stack][:-crates]

    for crate in crates_to_remove:
        stacks[to_stack].append(crate)

print("Answer to part 2: ", getStackEnds())        
