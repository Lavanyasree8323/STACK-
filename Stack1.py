from Stack import stack
# creating empty stack object
s=stack()
# display menu
choice =0
while choice <5:
    print('STACK OPERATION')
    print('1. Push element')
    print('2. Pop element')
    print('3. Peep element')
    print('4. Search for element')
    print('5. Exit')
    choice = int(input('Enter your choice:'))
    # Perform a task depending on user choice.
    if choice == 1:
        element = int(input('Enter the element:'))
        s.push(element)
    elif choice == 2:
        element = s.pop()
        if element == -1:
            print('The stack is empty')
        else:
            print('Popped Elements=',element)
    elif choice==3:
        element =s.peep()
        print('Topmost element=',element)
    elif choice == 4:
        element = int(input('Enter the element to search:'))
        pos = s.search(element)
        if pos == -1:
            print('The stack is empty')
        elif pos == -2:
             print('Element not found in stack')
        else:
            print('Element found at position:',pos)
    else:
        break
print('stack=',s.display())
