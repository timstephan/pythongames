# Menu to start the games
import os

print('''
                              mm                                                                                           
*@@@***@@m              @@   @@@                                     mm@***@m@                                             
  @@   *@@m             @@    @@                                   m@@*     *@                                             
  @@   m@@ *@@*   *@@*@@@@@@  @@@@@@@m    m@@*@@m *@@@@@@@@m       @@*       *  m@*@@m  *@@@@@@@@m@@@@@m    mm@*@@  m@@*@@@
  @@@@@@@    @@   m@    @@    @@    @@   @@*   *@@  @@    @@       @!          @@   @@    @@    @@    @@   m@*   @@ @@   **
  @@          @@ m!     @@    @@    @!   @@     @@  @!    @@       @!m    *@@@@ m@@@!@    !@    @@    @@   !@****** *@@@@@m
  @!           @@!      @!    @!    @!   @@     !@  @!    !@       *!@m     @@ @!   !@    !@    !@    @@   !@m    m      @@
  @!           @!!      !!    !!    !!   !@     !!  !!    !!       !!!    *!@!! !!!!:!    !!    !!    !!   !!****** *!   @!
  !!           !!:      !!    !:    !:   !!!   !!!  !!    !!       *:!!     !! !!   :!    :!    :!    !!   :!!      !!   !!
:!:!:          !!       ::: :: :   : : :  : : : : : :::  :!: :       ::: : ::  :!: : !: : :!:  :::   ::!:   : : ::  : :!:  
             ::!                                                                                                           
           :::                                                                                                             
''')

print("Please choose one game: ")
print("Type number to start game.")
print("1. tic tac toe")
print("2. Hangman the Game")
print("3. Exit")
i = int(input())

if i == 1:
    os.system('python tictactoe.py')
if i == 2:
    os.system('python Hangman_the_game.py')
if i == 3:
    print("Bye! See you soon.")
