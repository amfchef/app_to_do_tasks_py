from Add_to_dos import Add_to_dos
from Append import Append
print("Welcome to your ToDos app \nPlease enter from the menu below")

continue_loop = True


def return_to_main():
    global continue_loop
    error_input = str(input("Error \nInvalid menu choice\nWould you like to go back the menu: "
                            "Press [y] to go back \nOr any other letter to exit"))
    if error_input == "y" or "Y":
        continue_loop = True
    else:
        exit(0)


while continue_loop:
    menu_input = int(input("[1] Add new ToDo file and add your text"
                           "\n[2]Append to an existing file\n""[3] Read from an existing file"))
    if menu_input == 1:
        to_do = Add_to_dos()
        to_do.add_file()
        return_to_main()
    elif menu_input == 2:
        append = Append()
        append.append_file()
        return_to_main()
    elif menu_input == 3:

    else:
        return_to_main()

