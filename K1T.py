from cProfile import label
from tkinter import *
from time import *
import time
import random
from tracemalloc import start
from turtle import update
import math
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer
import re 

while True:
    print('==================')
    print('Kit de herramientas')
    print('===================\n')
    print('Creado por P1rs0n.')
    nombre = input('Introduce tu nombre:')
    print('Hola {} en este programa tendras diferentes herramientas para utilizar.'.format(nombre))

    print('Menu de opciones:\n')
    print('Presiona 1 para convertir de numero a palabra.')
    print('Presiona 2 para convertir de palabra a numero.')
    print('Presiona 3 para calcular tu promedio.')
    print('Presione 4 para generar una cuenta atras de 10 segundos.')
    print('Presione 5 para generar un numero aleatorio de 1 a 10.')
    print('Presione 6 para jugar Piedra, Papel o Tijeras')
    print('Presione 7 para jugar un juego de Quiz simple')
    print('Presione 8 para ver la hora.')
    print('Presione 9 para usar la calculadora')
    print('Presione 10 para jugar tres en raya')
    print('Presione 11 para jugar buscaminas')
    print('Presione 12 para dejar de usar el kit\n')

    opcion = int(input('Digite aqui:'))

    if opcion == 1:
        print('====================================')
        print('\n Conversor de numero a palabra.\n')
        print('====================================')
        eleccion = int(input('Cual es el numero que deseas convertir?: '))
        if eleccion == 1:
            print('Uno')
        elif eleccion == 2:
            print('Dos')
        elif eleccion == 3:
            print("Tres")
        elif eleccion == 4:
            print("Cuatro")
        elif eleccion == 5:
            print('Cinco')
        else:
            print('Solo se pueden convertir numeros del 1 al 5!')

    elif opcion == 2:
        print('====================================')
        print('\n conversor de palabra a numero.\n ')
        print('====================================')
        eleccion = input('Cual es la palabra que deseas convertir?: ')

        if eleccion == 'Uno':
            print('1')
        elif eleccion == 'Dos':
            print('2')
        elif eleccion == 'Tres':
            print("3")
        elif eleccion == 'Cuatro':
            print("4")
        elif eleccion == 'Cinco':
            print('5')
        else:
            print('Solo se pueden convertir numeros del 1 al 5!')

    elif opcion == 3:

        print('=======================')
        print('Calculador de promedio')
        print('=======================\n')
        print('En este programa podras calcular el promedio de tu calificacion en base a 100.')
        espa = int(input('Introduce tu calificacion en Gramatica:'))
        mate = int(input('Introduce tu calificacion en Matematicas:'))
        soci = int(input('Introduce tu calificacion en Sociales:'))
        vida = int(input('Introduce tu calificacion en Ciencias de la vida:'))
        ing = int(input('Introduce tu calificacion en Ingles:'))
        fr = int(input('Introduce tu calificacion en Frances:'))
        fihr = int(input('Introduce tu calificacion en Religion:'))
        arte = int(input('Introduce tu calificacion en Arte:'))
        fisi = int(input('Introduce tu calificacion en Deportes:'))
        desa = int(input('Introduce tu calificacion en Desarollo Humano:'))
        infogod = int(input('Introduce tu calificacion en Informatica:'))

        promedio = (espa+mate+soci+vida+ing+fr+fihr+arte+fisi+desa+infogod) / 11

        print('Felicidades, tu promedio fue de ', promedio)

        compo = int(input('Introduce tu comportamiento:'))
        respo = int(input('Introduce tu responsabilidad:'))
        urb = int(input('Introduce tu urbanidad:'))

        ajuste = (compo+respo+urb) / 3
        print('Tu promedio de Ajuste Personal es:', ajuste)
        promediof = (promedio+ajuste) / 2

        print('Tu promedio de 2do de Secundaria fue:')
        time.sleep(2)
        print('cargando........')
        time.sleep(2)
        print('cargando ****....')
        time.sleep(2) 
        print('cargando *******')
        print(promediof)

        if promediof >= 90 and promediof <= 93.3333:
            print('Felicidades, sacaste cartoncito')
        elif promediof >= 93.44 and promediof <= 95.5:
            print('Felicidades sacaste medalla al merito!')
        elif promediof >= 95.6 and promediof <= 99.7:
            print('Felicidades, estas engordando!')
        elif promediof >= 99.8:
            print('Felicidades, eres el rey gordo!!!')
        elif promediof < 90:
            print('Tranquilo la proxima sera la vencida!')

    elif opcion == 4:
            print('=============')
            print('Cuenta Regresiva')
            print('=============')
            for seconds in range(10,0,-1):
                print(seconds)
                time.sleep(1)

    elif opcion == 5:
        x = random.randint(1,10)
        print(x)

    elif opcion == 6:

        while True:
            choices = ["rock", "paper", "scissors"]

            computer = random.choice(choices)
            player = None

            while player not in choices:
                player = input("rock, paper, or scissors?: ").lower()

            if player == computer:
                print("computer: ", computer)
                print("player: ", player)
                print("Tie!")

            elif player == "rock":
                if computer == "paper":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You lose!")
                if computer == "scissors":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You win!")

            elif player == "scissors":
                if computer == "rock":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You lose!")
                if computer == "paper":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You win!")

            elif player == "paper":
                if computer == "scissors":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You lose!")
                if computer == "rock":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You win!")

            play_again = input("Play again? (yes/no): ").lower()

            if play_again != "yes":
                break

        print("Bye!")

    elif opcion == 7:


        def new_game():

            respuestas = []
            respuestas_correctas = 0
            num_preguntas = 1

            for key in preguntas:
                print('---------------------')
                print(key)
                for i in opciones[num_preguntas-1]:
                    print(i)
                guess = input('Elige (A,B,C,D)')
                guess = guess.upper()
                respuestas.append(guess)

                respuestas_correctas += check_answer(preguntas.get(key), guess)
                num_preguntas += 1

            display_score(respuestas_correctas, respuestas)
        def check_answer(answer, guess):

            if answer == guess:
                print('Correcto!')
                return 1
            else:
                print('Incorrecto!')
                return 0

        def display_score(respuestas_correctas, respuestas):
            print('---------------------')
            print('RESULTADOS')
            print('---------------------')

            print('Preguntas: ', end='')
            for i in preguntas:
                print(preguntas.get(i), end=' ')
            print()

            print('Respuestas: ', end='')
            for i in respuestas:
                print(i, end=' ')
            print()

            resultado = int((respuestas_correctas / len(preguntas))*100)
            print('Tus resultados fueron: '+str(resultado)+'%')

        def play_again():

           response = input('Quieres jugar de nuevo?: (si o no):')
           response = response.upper()
           if response == 'SI':
               return True
           else:
               return False


        preguntas = {
            'Quien creo Python?:':'A',
            'Cuando se creo Python?:':'B',
            'Quien es el CEO de Tesla?:': 'D',
            'La tierra es redonda?:': 'A'
        }
        opciones = [["A. Guido van Rossum", "B. Lebron James", "C. Tutankamon", "D. Juan Carlos"],
                   ["A. 1989", "B. 1991", "C. no se ", "D. 2016"],
                   ["A. Bill Gates", "B. Elon Musk", "C. Que se yo", "D. Michael Jordan"],
                   ["A. Si", "B. No", "C. Belony Bruno", "D. ok"]]
        new_game()
        while play_again():
            new_game()
        print('Bye.')

    elif opcion == 8:
        def update():
            time_string = strftime("%I:%M:%S %p")
            time_label.config(text=time_string)

            day_string = strftime("%A")
            day_label.config(text=day_string)

            date_string = strftime("%B %d, %Y")
            date_label.config(text=date_string)

            window.after(1000,update)


        window = Tk()
        window.title = ("Reloj")

        time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
        time_label.pack()

        day_label = Label(window,font=("Ink Free",25,"bold"))
        day_label.pack()

        date_label = Label(window,font=("Ink Free",30))
        date_label.pack()

        update()

        window.mainloop()



    elif opcion == 9:
        def button_press(num):

            global equation_text

            equation_text = equation_text + str(num)

            equation_label.set(equation_text)

        def equals():

            global equation_text

            try:

                total = str(eval(equation_text))

                equation_label.set(total)

                equation_text = total

            except SyntaxError:

                equation_label.set("ES UNA CALCULADORA MIO")

                equation_text = ""

            except ZeroDivisionError:

                equation_label.set("MMG NO PUEDES DIVIDIR ENTRE 0")

                equation_text = ""

        def clear():

            global equation_text

            equation_label.set("")

            equation_text = ""


        window = Tk()
        window.title("Calculadora")
        window.geometry("1024x768")

        equation_text = ""

        equation_label = StringVar()

        label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
        label.pack()

        frame = Frame(window)
        frame.pack()

        button1 = Button(frame, text=1, height=4, width=9, font=35,
                         command=lambda: button_press(1))
        button1.grid(row=0, column=0)

        button2 = Button(frame, text=2, height=4, width=9, font=35,
                         command=lambda: button_press(2))
        button2.grid(row=0, column=1)

        button3 = Button(frame, text=3, height=4, width=9, font=35,
                         command=lambda: button_press(3))
        button3.grid(row=0, column=2)

        button4 = Button(frame, text=4, height=4, width=9, font=35,
                         command=lambda: button_press(4))
        button4.grid(row=1, column=0)

        button5 = Button(frame, text=5, height=4, width=9, font=35,
                         command=lambda: button_press(5))
        button5.grid(row=1, column=1)

        button6 = Button(frame, text=6, height=4, width=9, font=35,
                         command=lambda: button_press(6))
        button6.grid(row=1, column=2)

        button7 = Button(frame, text=7, height=4, width=9, font=35,
                         command=lambda: button_press(7))
        button7.grid(row=2, column=0)

        button8 = Button(frame, text=8, height=4, width=9, font=35,
                         command=lambda: button_press(8))
        button8.grid(row=2, column=1)

        button9 = Button(frame, text=9, height=4, width=9, font=35,
                         command=lambda: button_press(9))
        button9.grid(row=2, column=2)

        button0 = Button(frame, text=0, height=4, width=9, font=35,
                         command=lambda: button_press(0))
        button0.grid(row=3, column=0)

        plus = Button(frame, text='+', height=4, width=9, font=35,
                         command=lambda: button_press('+'))
        plus.grid(row=0, column=3)

        minus = Button(frame, text='-', height=4, width=9, font=35,
                         command=lambda: button_press('-'))
        minus.grid(row=1, column=3)

        multiply = Button(frame, text='*', height=4, width=9, font=35,
                         command=lambda: button_press('*'))
        multiply.grid(row=2, column=3)

        divide = Button(frame, text='/', height=4, width=9, font=35,
                         command=lambda: button_press('/'))
        divide.grid(row=3, column=3)

        equal = Button(frame, text='=', height=4, width=9, font=35,
                         command=equals)
        equal.grid(row=3, column=2)

        decimal = Button(frame, text='.', height=4, width=9, font=35,
                         command=lambda: button_press('.'))
        decimal.grid(row=3, column=1)

        clear = Button(window, text='clear', height=4, width=12, font=35,
                         command=clear)
        clear.pack()

        window.mainloop()

    elif opcion == 10:
        class TicTacToe():
            def __init__(self):
                self.board = self.make_board()
                self.current_winner = None

            @staticmethod
            def make_board():
                return [' ' for _ in range(9)]

            def print_board(self):
                for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
                    print('| ' + ' | '.join(row) + ' |')

            @staticmethod
            def print_board_nums():
                # 0 | 1 | 2
                number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
                for row in number_board:
                    print('| ' + ' | '.join(row) + ' |')

            def make_move(self, square, letter):
                if self.board[square] == ' ':
                    self.board[square] = letter
                    if self.winner(square, letter):
                        self.current_winner = letter
                    return True
                return False

            def winner(self, square, letter):
                # check the row
                row_ind = math.floor(square / 3)
                row = self.board[row_ind*3:(row_ind+1)*3]
                # print('row', row)
                if all([s == letter for s in row]):
                    return True
                col_ind = square % 3
                column = [self.board[col_ind+i*3] for i in range(3)]
                # print('col', column)
                if all([s == letter for s in column]):
                    return True
                if square % 2 == 0:
                    diagonal1 = [self.board[i] for i in [0, 4, 8]]
                    # print('diag1', diagonal1)
                    if all([s == letter for s in diagonal1]):
                        return True
                    diagonal2 = [self.board[i] for i in [2, 4, 6]]
                    # print('diag2', diagonal2)
                    if all([s == letter for s in diagonal2]):
                        return True
                return False

            def empty_squares(self):
                return ' ' in self.board

            def num_empty_squares(self):
                return self.board.count(' ')

            def available_moves(self):
                return [i for i, x in enumerate(self.board) if x == " "]


        def play(game, x_player, o_player, print_game=True):

            if print_game:
                game.print_board_nums()

            letter = 'X'
            while game.empty_squares():
                if letter == 'O':
                    square = o_player.get_move(game)
                else:
                    square = x_player.get_move(game)
                if game.make_move(square, letter):

                    if print_game:
                        print(letter + ' mueve a la casilla {}'.format(square))
                        game.print_board()
                        print('')

                    if game.current_winner:
                        if print_game:
                            print(letter + ' Gana!')
                        return letter  
                    letter = 'O' if letter == 'X' else 'X'  

                time.sleep(.8)


        if __name__ == '__main__':
            x_player = SmartComputerPlayer('X')
            o_player = HumanPlayer('O')
            t = TicTacToe()
            play(t, x_player, o_player, print_game=True)

    elif opcion == 11:
     
        class Board:
            def __init__(self, dim_size, num_bombs):
                
                self.dim_size = dim_size
                self.num_bombs = num_bombs

               
                self.board = self.make_new_board() 
                self.assign_values_to_board()

                
                self.dug = set() 

            def make_new_board(self):
              

               
                board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
            
                bombs_planted = 0
                while bombs_planted < self.num_bombs:
                    loc = random.randint(0, self.dim_size**2 - 1) 
                    row = loc // self.dim_size 
                    col = loc % self.dim_size  

                    if board[row][col] == '*':
                        
                        continue

                    board[row][col] = '*' 
                    bombs_planted += 1

                return board

            def assign_values_to_board(self):
                
                for r in range(self.dim_size):
                    for c in range(self.dim_size):
                        if self.board[r][c] == '*':
                            
                            continue
                        self.board[r][c] = self.get_num_neighboring_bombs(r, c)

            def get_num_neighboring_bombs(self, row, col):
         
                num_neighboring_bombs = 0
                for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                    for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                        if r == row and c == col:
                            
                            continue
                        if self.board[r][c] == '*':
                            num_neighboring_bombs += 1

                return num_neighboring_bombs

            def dig(self, row, col):


                self.dug.add((row, col)) 

                if self.board[row][col] == '*':
                    return False
                elif self.board[row][col] > 0:
                    return True

              
                for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                    for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                        if (r, c) in self.dug:
                            continue
                        self.dig(r, c)


                return True

            def __str__(self):

                visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
                for row in range(self.dim_size):
                    for col in range(self.dim_size):
                        if (row,col) in self.dug:
                            visible_board[row][col] = str(self.board[row][col])
                        else:
                            visible_board[row][col] = ' '

                string_rep = ''
                
                widths = []
                for idx in range(self.dim_size):
                    columns = map(lambda x: x[idx], visible_board)
                    widths.append(
                        len(
                            max(columns, key = len)
                        )
                    )

                indices = [i for i in range(self.dim_size)]
                indices_row = '   '
                cells = []
                for idx, col in enumerate(indices):
                    format = '%-' + str(widths[idx]) + "s"
                    cells.append(format % (col))
                indices_row += '  '.join(cells)
                indices_row += '  \n'

                for i in range(len(visible_board)):
                    row = visible_board[i]
                    string_rep += f'{i} |'
                    cells = []
                    for idx, col in enumerate(row):
                        format = '%-' + str(widths[idx]) + "s"
                        cells.append(format % (col))
                    string_rep += ' |'.join(cells)
                    string_rep += ' |\n'

                str_len = int(len(string_rep) / self.dim_size)
                string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

                return string_rep

     
        def play(dim_size=10, num_bombs=10):
          
            board = Board(dim_size, num_bombs)


            safe = True 

            while len(board.dug) < board.dim_size ** 2 - num_bombs:
                print(board)

                user_input = re.split(',(\\s)*', input("Donde quisieras cavar? Escribe en este formato fila,col Ejemplo: 0,0: "))  # '0, 3'
                row, col = int(user_input[0]), int(user_input[-1])
                if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
                    print("Invalid location. Try again.")
                    continue


                safe = board.dig(row, col)
                if not safe:

                    break 

            if safe:
                print("FELICIDADADES!!!!!!!! GANASTE")
            else:
                print("BOZOOOOOO")

                board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
                print(board)

        if __name__ == '__main__': 
            play()
    elif opcion == 12:
        print('Gracias por usar el kit :)')
        break
