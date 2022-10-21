
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True# You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()


try:

    player1_board= [["-"for i in range(board_size)] for j in range(board_size)]         #player1 ve player 2 nin tahtası ve bunların gizli tahtaları
    player2_board= [["-" for z in range(board_size)] for t in range(board_size)]
    player1_fake_board = [["-" for i in range(board_size)] for j in range(board_size)]
    player2_fake_board = [["-" for i in range(board_size)] for j in range(board_size)]


    player1_ships=["Carrier","Battleship","Cruiser","Submarine","Destroyer"]
    player2_ships=["Carrier","Battleship","Cruiser","Submarine","Destroyer"]
    lenght={"Carrier":5,"Battleship":4,"Cruiser":3,"Submarine":3,"Destroyer":2}


    turn1=True
    turn2=False




    while turn1:
            list = [player1_board, player2_fake_board] #burda tahtayı yazdırıyoruz
            print_3d_list(my_list=list)

            y = False
            print_ships_to_be_placed()

            for k in player1_ships:           #gemileri yazdırıyoruz
                print_single_element(elem=k)

            print_empty_line()

            print_player_turn_to_place(1)

            print_to_place_ships()

            x =input()

            cordinats=x.split() # inputu listeye atıyoruz
            if len(cordinats) < 4:
                print_incorrect_input_format()          #burdaki kodlarda hata durumlarında while dongusunde başa donduruyoruz ki tahta tekrar yüklensin
                continue
            cordinats[0]=cordinats[0].capitalize()

            try:
                int(cordinats[1])   # tamsayı mı diye bakıyoruz
            except:
                print_incorrect_input_format()
                continue

            try:
                int(cordinats[2])
            except:
                print_incorrect_input_format()
                continue

            if int(cordinats[1]) > 10:  # kordinatlar tahtadann büyükse
                print_incorrect_coordinates()
                continue
            if int(cordinats[2]) > 10:
                print_incorrect_coordinates()
                continue

            if int(cordinats[1]) < 1 or int(cordinats[2]) < 1:  # kordinatlar 0 dan küçükse
                print_incorrect_coordinates()
                continue

            if cordinats[0] not in player1_ships:    #gemi inputta yanlışsa veya yoksa durumunu inceliyoruz
                if cordinats[0] in lenght:
                    print_ship_is_already_placed(cordinats[0])
                    continue
                else:
                    print_incorrect_ship_name()
                    continue


            if cordinats[3] not in ['h', 'H', 'v', 'V']:   # yatay veya dikey komutu yoksa hata olur
                print_incorrect_orientation()
                continue



            if len(cordinats)>4:               # listedeki eleman sayısı 4 te nküçükse tabiki hata oluşur
                for i in cordinats[5:len(cordinats)+1]:
                    cordinats.remove(i)


            if cordinats[3] == 'h' or cordinats[3] == 'H':       # burda gemiyi koyduğumuzda tahtanın dışına taşmamasını garanti ediyoruz
                if int(lenght[cordinats[0]]) + int(cordinats[1]) > 11 :
                    print_ship_cannot_be_placed_outside(cordinats[0])
                    continue

            if cordinats[3] == 'v' or cordinats[3] == 'V':        #burda gemiyi koyduğumuzda tahtanın dışına taşmamasını garanti ediyoruz
                if int(lenght[cordinats[0]]) + int(cordinats[2]) > 11 :
                    print_ship_cannot_be_placed_outside(cordinats[0])
                    continue




            if cordinats[3] == 'v' or cordinats[3] == 'V': # burda gemilerin aynı bölgeyi kaplamadığından emin oluyoruz
                for i in range(int(lenght[cordinats[0]])):

                    if player1_board[int(cordinats[2]) + i - 1][int(cordinats[1]) - 1] == '#':
                        print_ship_cannot_be_placed_occupied(cordinats[0])
                        y = True
                        break


            if cordinats[3] == 'h' or cordinats[3] == 'H':# burda gemilerin aynı bölgeyi kaplamadığından emin oluyoruz
                for i in range(int(lenght[cordinats[0]])):

                    if player1_board[int(cordinats[2]) - 1][i + int(cordinats[1]) - 1] == '#':
                        print_ship_cannot_be_placed_occupied(cordinats[0])
                        y = True
                        break


            if y :
                continue

            if cordinats[3] == 'h' or cordinats[3] == 'H':          #geminin dışarı taşmasını engelliyoruz
                if int(lenght[cordinats[0]]) + int(cordinats[1]) > 11 or int(cordinats[2]) >10:
                    print_ship_cannot_be_placed_outside(cordinats[0])
                    continue

            if cordinats[3] == 'v' or cordinats[3] == 'V':  #geminin dışarı taşmasını engelliyoruz
                if int(lenght[cordinats[0]]) + int(cordinats[2]) > 11 or int(cordinats[1]) >10:
                    print_ship_cannot_be_placed_outside(cordinats[0])
                    continue


            if cordinats[0] in player1_ships:
                y = False

                if cordinats[3]=='h' or cordinats[3]=='H':# burda gemileri yazdırıyoruz
                    for i in range(int(lenght[cordinats[0]])):

                        player1_board[int(cordinats[2])-1][i+int(cordinats[1])-1]='#'


                if cordinats[3]=='v' or cordinats[3]=='V':# burda gemiler iyazdırıyoruz
                    for i in range(int(lenght[cordinats[0]])):

                        player1_board[int(cordinats[2]) +i -1][int(cordinats[1]) - 1] = '#'


                player1_ships.remove(cordinats[0])
            else:
                print_incorrect_ship_name()
                continue


            if len(player1_ships)==0:  #eğer geriye gemi kalmadıysa yes veya no inputu alıp sırayı 2.ye geçiriyor
                print_3d_list(my_list=list)

                b = True
                while b:
                    print_confirm_placement()
                    z = str(input())

                    if z.strip() == 'y' or z.strip() == 'Y':
                        turn2 = True
                        turn1 = False
                        b = False
                        k = False
                        break

                    if z.strip() == 'n' or z.strip() == 'N':
                        player1_ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                        player1_board = [["-" for i in range(board_size)] for j in range(board_size)]
                        b = False
                        k = True
                        continue

                    else:
                        b = True
                        continue

                if k == True:
                    continue


    while turn2:         # ikinci adamın kodu 1.deki ile tıpatıp aynıdır sadec son bölümde ufak bir değişiklik var

        list=[player1_fake_board,player2_board]
        print_3d_list(my_list=list)
        print_ships_to_be_placed()

        y = False


        for j in player2_ships:
            print_single_element(elem=j)

        print_empty_line()

        print_player_turn_to_place(2)

        print_to_place_ships()

        x = input()

        cordinats = x.split()
        if len(cordinats) < 4:
            print_incorrect_input_format()
            continue
        cordinats[0] = cordinats[0].capitalize()

        try:
            int(cordinats[1])
        except:
            print_incorrect_input_format()
            continue

        try:
            int(cordinats[2])
        except:
            print_incorrect_input_format()
            continue

        if int(cordinats[1]) > 10:  # kordinatlar tahtadann büyükse
            print_incorrect_coordinates()
            continue
        if int(cordinats[2]) > 10:
            print_incorrect_coordinates()
            continue

        if int(cordinats[1]) < 1 or int(cordinats[2]) < 1:  # kordinatlar 0 dan küçükse
            print_incorrect_coordinates()
            continue


        if cordinats[0] not in player2_ships:
            if cordinats[0] in lenght:
                print_ship_is_already_placed(cordinats[0])
                continue
            else:
                print_incorrect_ship_name()
                continue


        if cordinats[3] not in ['h', 'H', 'v', 'V']:
            print_incorrect_orientation()
            continue



        if len(cordinats) > 4:
            for i in cordinats[5:len(cordinats) + 1]:
                cordinats.remove(i)



        if cordinats[3] == 'h' or cordinats[3] == 'H':
            if int(lenght[cordinats[0]]) + int(cordinats[1])>11 or int(cordinats[2])> 10:
                print_ship_cannot_be_placed_outside(cordinats[0])
                continue

        if cordinats[3] == 'v' or cordinats[3] == 'V':
            if int(lenght[cordinats[0]]) + int(cordinats[2]) > 11 or int(cordinats[1]) >10:
                print_ship_cannot_be_placed_outside(cordinats[0])
                continue

        if cordinats[3] == 'v' or cordinats[3] == 'V':
            for i in range(int(lenght[cordinats[0]])):

                if player2_board[int(cordinats[2]) + i - 1][int(cordinats[1]) - 1] == '#':
                    print_ship_cannot_be_placed_occupied(cordinats[0])
                    y = True
                    break

        if cordinats[3] == 'h' or cordinats[3] == 'H':
            for i in range(int(lenght[cordinats[0]])):

                if player2_board[int(cordinats[2]) - 1][i + int(cordinats[1]) - 1] == '#':
                    print_ship_cannot_be_placed_occupied(cordinats[0])

                    y = True
                    break

        if y:
            continue


        if cordinats[3] == 'h' or cordinats[3] == 'H':
            if int(lenght[cordinats[0]]) + int(cordinats[1]) > 11:
                print_ship_cannot_be_placed_outside(cordinats[0])
                continue

        if cordinats[3] == 'v' or cordinats[3] == 'V':
            if int(lenght[cordinats[0]]) + int(cordinats[2]) > 11:
                print_ship_cannot_be_placed_outside(cordinats[0])
                continue


        if int(cordinats[1]) > 10 or int(cordinats[1]) > 10:
            print_incorrect_coordinates()
            continue

        if int(cordinats[1]) < 1 or int(cordinats[2]) < 1:
            print_incorrect_coordinates()
            continue

        if cordinats[0] in player2_ships:
            y = False

            if cordinats[3] == 'h' or cordinats[3] == 'H':
                for i in range(int(lenght[cordinats[0]])):
                    player2_board[int(cordinats[2]) - 1][i + int(cordinats[1]) - 1] = '#'

            if cordinats[3] == 'v' or cordinats[3] == 'V':
                for i in range(int(lenght[cordinats[0]])):
                    player2_board[int(cordinats[2]) + i - 1][int(cordinats[1]) - 1] = '#'

            player2_ships.remove(cordinats[0])
        else:
            print_incorrect_ship_name()
            continue

        if len(player2_ships) == 0:
            print_3d_list(my_list=list)
            b=True
            while b:
                print_confirm_placement()
                z = str(input())

                if z.strip() == 'y' or  z.strip()=='Y':
                    turn2 = False
                    b=False
                    l=False
                    break


                if z.strip() =='n' or z.strip()=='N':
                    player2_ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]   #eğer yes ise savaş bölümüne geçiriyor no ise tekrar savaş tahtasını yüklüyor
                    player2_board = [["-" for i in range(board_size)] for j in range(board_size)]
                    b=False
                    l=True
                    continue

                else:
                    b=True
                    continue

            if l ==True:
                continue




    #oyun aşaması vuruşlar.
    war =True
    player1_turn=True
    player2_turn=False
    while war:
        while player1_turn:
            list=[player1_board,player2_fake_board]  #1.adamın savaş turu



            print_3d_list(list)
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            u=input().strip()
            target_cordiantes=u.split()

            if len(target_cordiantes )< 2:    # ilk olarak hataları ayıkladım
                print_incorrect_input_format()
                continue

            if len(target_cordiantes )> 2:
                for i in target_cordiantes[3:len(target_cordiantes)+1]:
                    target_cordiantes.remove(i)


            try:
                int(target_cordiantes[1])
                int(target_cordiantes[0])
            except:
                print_incorrect_input_format()
                continue

            if int(target_cordiantes[0])>10:
                print_incorrect_coordinates()
                continue
            if int(target_cordiantes[1])>10:
                print_incorrect_coordinates()
                continue
            if int(target_cordiantes[0])<1:
                print_incorrect_coordinates()
                continue

            if int(target_cordiantes[1])<1 :
                print_incorrect_coordinates()
                continue

            if player2_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] == 'O' or  player2_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] == '!':
                print_tile_already_struck()
                continue

                #yukardaki bölümde vurulan yerin tekrar vurulması halinde uyarı vermesi sağlanıyor


            if player2_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] == '#': #vurduysak hit yazıyor ve ! koyuyor
                print_hit()
                player2_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] = '!'
                player2_fake_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] = '!'

                x = 0
                for i in player2_board:  # burda oyunun ne zaman biteceğine karar veriyoruz eğer hiç bir listede # yoksa oyun biter
                    if '#' not in i:   # burda tahtadaki nested listin içindeki elemmanlarda # olup olmadığına bakıyoruz
                        x = x + 1
                    if x == board_size:
                        print_3d_list(list)
                        print_player_won(1)
                        print_thanks_for_playing()
                        war = False
                        a = False
                        player2_turn = False
                        player1_turn = False


                continue


            if player2_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] == '-': # burda da vuramadıysak miss yazdırıyor ve O koyuyor
                player2_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] = 'O'
                player2_fake_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] = 'O'
                print_miss()


            a=bool
            while a:
                print_type_done_to_yield(2)    #type doneın tekrar etmesini sağlayan kod
                z = input().strip().capitalize()
                if z == 'Done':
                    a = False
                    player1_turn = False
                    player2_turn = True





        while player2_turn:      #player 2 turu player 1 ile tamamen aynı

            list=[player1_fake_board, player2_board]

            print_3d_list(list)
            print_player_turn_to_strike(2)
            print_choose_target_coordinates()
            u = input().strip()
            target_cordiantes = u.split()
            if len(target_cordiantes)<2:
                print_incorrect_input_format()
                continue

            if len(target_cordiantes)>2:
                for i in target_cordiantes[3:len(target_cordiantes)+1]:
                    target_cordiantes.remove(i)
            try:
                int(target_cordiantes[1])
                int(target_cordiantes[0])
            except:
                print_incorrect_input_format()
                continue

            if int(target_cordiantes[0])>10:
                print_incorrect_coordinates()
                continue
            if int(target_cordiantes[1])>10:
                print_incorrect_coordinates()
                continue
            if int(target_cordiantes[0])<1:
                print_incorrect_coordinates()
                continue

            if int(target_cordiantes[1])<1 :
                print_incorrect_coordinates()
                continue


            if player1_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] == 'O' or player1_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] == '!':
                print_tile_already_struck()
                continue


            if player1_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] == '#':
                print_hit()
                player1_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] = '!'
                player1_fake_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] = '!'
                x=0
                for i in player1_board:
                    if '#' not in i:
                        x = x + 1
                    if x == board_size:
                        print_3d_list(list)
                        print_player_won(2)
                        print_thanks_for_playing()
                        war = False
                        a = False
                        player2_turn = False
                        player1_turn = False
                continue


            if player1_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] == '-':
                player1_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] = 'O'
                player1_fake_board[int(target_cordiantes[1]) - 1][int(target_cordiantes[0]) - 1] = 'O'
                print_miss()


            a=True
            while a:
                print_type_done_to_yield(1)
                z = input().strip().capitalize()
                if z == 'Done':

                    a=False
                    player1_turn = True
                    player2_turn = False


    
except:
    f.close()





