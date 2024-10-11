
stack_star = []
stack_volcono = []
stack_ritco = []

def push_tracker(stack, tracker):
    print(f"Registering '{tracker}' to {stack}...")
    if stack == "star":
        stack_star.append(tracker)
    elif stack== "volcano":
        stack_volcono.append(tracker)
    elif stack == "ritico":
        stack_ritco.append(tracker)

    print(f" {stack}  {stack_star if stack == 'star' else stack_volcono if stack == 'volcono' else stack_ritco}")


def pop_tracker(stack):
    print(f" {stack}...")
    if stack == "star" and stack_star:
        removed_tracker = stack_star.pop()
        print(f"Removed tracker: {removed_tracker}")
    elif stack== "volcono" and stack_volcono:
        removed_tracker = stack_volcono.pop()
        print(f"Removed tracker: {removed_tracker}")
    elif stack == "ritco" and stack_ritco:
        removed_tracker = stack_ritco.pop()
        print(f"Removed tracker: {removed_tracker}")
    else:
        print(f" {stack}")
        return

    print(f" {stack}  {stack_star if stack == 'star' else stack_volcono if stack == 'volcono' else stack_ritco}")
stack_star = []
stack_volcono = []
stack_ritco= []

def push_stack(stack, tracker):
    print(f" '{stack}' to {tracker}...")
    if stack == "star":
        stack_star.append(stack)
    elif stack == "volcono":
        stack_volcono.append(stack)
    elif stack == "ritco":
        stack_ritco.append(stack)
    
    print(f" {stack} stack {stack_star if stack == 'star' else stack_volcono if stack == 'volcono' else stack_ritco}")


def pop_stack(stack):

    print(f" {stack}")
    if stack == "star" and stack_star:
        removed_stack = stack_star.pop()
        print(f"Removed stack: {removed_stack}")
    elif stack == "volcono" and stack_volcono:
        removed_stack = stack_volcono.pop()
        print(f"Removed stack: {removed_stack}")
    elif stack == "ritco" and stack_ritco:
        removed_stack = stack_ritco.pop()
        print(f"Removed stack: {removed_stack}")
    else:
        print(f"N{stack}")
        return

    print(f" {stack}  {stack_star if stack == 'star' else stack_volcono if stack == 'volcono' else stack_ritco}")


push_stack("star","")
push_stack("volcano","")
push_stack("ritco", "ritco")


pop_stack("star")
pop_stack("volcono")
pop_stack("ritco")


