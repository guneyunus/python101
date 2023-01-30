todos = []

while True:
    user_action = input('Type show or add: ')

    match user_action.strip():
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo.strip())
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case x:
            print('You entered an unknown command.')

print('Bye!')
