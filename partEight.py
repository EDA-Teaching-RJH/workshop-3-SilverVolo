running = True
inventory = []
position = [2,1]
def openInventory(quantity, moves):
    if quantity == 1:
        print(moves)
    elif quantity == 2:
        lastMove = moves.pop()
        moves.append(lastMove)
        print(lastMove)
    
def move(current_position, direction):

    if direction == "N":
        current_position[1] += 1
        return current_position
    if direction == "E":
        current_position[0] += 1
        return current_position
    if direction == "S":
        current_position[1] -= 1
        return current_position
    if direction == "W":
        current_position[0] -= 1
        return current_position
    
        

    

while running:
    
    
    print("""###Forest###\n
          
          You are in lost in a forest. Find a way to escape.\n
          You can proceed north, east, south or west\n
          Type N, E, S, W to indiciate your decision""")
    decision = input(": ")
    inventory.append(decision)
    choice = int(input("""What will you do now?\n 
                   1. Move\n
                   2. Check previous moves\n
                   3. Quit\n"""))
    if choice == 1:
        position = move(position, decision)
        print(position)
        if position == [0,2]:
            print("You escaped")
            running = False
    elif choice == 2:
        invChoice = int(input("""Do you want to see all of your past moves or just the last one?\n
              1. All\n
              2. Last one\n"""))
        openInventory(invChoice,inventory)
    else:
        running = False
    

    
    
