instructions = """
This will be our tic tac toe board
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
 """
 
sign_dictionary = []
for i in range(9):
 sign_dictionary.append(' ')

def print_board():
    board = f"""

 {sign_dictionary[0]} | {sign_dictionary[1]} | {sign_dictionary[2]}
---|---|---
 {sign_dictionary[3]} | {sign_dictionary[4]} | {sign_dictionary[5]}
---|---|---
 {sign_dictionary[6]} | {sign_dictionary[7]} | {sign_dictionary[8]}
 """
def take_input(player_one):
    while True:
        x=int(input(f"{player_name}: "))
        x-=1
        if 0<= x < 10:
            if x in index_list:
                print("This spot is blocked.")
                continue
            index_list.append(x)
            return(x)
        print("please enter numer between 1-9")
def calculate_result(player_one,player_two):
    if sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'X' or
sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'X' or
sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'X' or
sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'X' or
sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'X' or
sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'X' or
sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'X' or
sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'X' :
    print(f"Congradulations{player_one}.!!! You Won.!")
    quit("Thank you both for joining.")
elif sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'O' or
sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'O' or
sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'O' or
sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'O' or
sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'O' or
sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'O' or
sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'O' or
sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'O' :
    print(f"Congradulations{player_two}.!!! You Won.!")
    quit("Thank you both for joining.")

   
def main():
    print("Welcome to Tic Tac Toe game..!!")
    player_one=input("Enter player one name: ")
    player_two=input("Enter player two name: ")
    print(f"Thank you for joining {player_one} and {player_two}")

    print(instructions)
    print(f"{player_one}'s sign will be - X")
    print(f"{player_two}'s sign will be - 0")
    input("Enter any key to start the game")

    print_board()
    for i in range(9):
        if i%2 == 0:
            index=take_input{player_one}
            sign_dictionary[index]='X'
        else:
            index=take_input{player_two}
            sign_dictionary[index]='O'
        print_board()
        calculate_result(player_one,player_two)
    print("This is a TIE,Nobody Won.Play Again.")
main()





















            
