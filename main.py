player1=input("Who is player1? A.K.A X :")
print("Hi," ,player1)
player2=input("Who is player2? A.K.A O :")
print("Hi,", player2)
print("Welcome,", player1 ,"and", player2)

print(" |     |")
print("-+-+-+-+-")
print(" |     |")
print("-+-+-+-+-")
print(" |     |")
turn = 'X'

board = [" ", " "," "," "," "," "," "," "," "]
count = 1
while count<10:

 pos = int(input("Enter the position where you wish to place the X/O: "))
 if board[pos] == " ":
  board[pos] = turn  
  count = count + 1
  if turn == 'X':
     turn = 'O'
  else:
    turn = 'X' 
 else:
     print("It is already occupied") 
 print(board[0],"|",board[1],"|",board[2])
 print("-+-+-+-+-")
 print(board[3],"|",board[4],"|",board[5])
 print("-+-+-+-+-")
 print(board[6],"|",board[7],"|",board[8])
 
 if count>=5:
     if board[0] == board[1] == board[2] != " ":
         print(board[0] , "WON! ")
         break
     elif board[3] == board[4] == board[5] != " ":
         print(board[3] , "WON! ")
         break
     elif board[6] == board[7] == board[8] != " ":
         print(board[6] , "WON!")
         break 
     elif board[0] == board[3] == board[6] != " ":
         print(board[6] , "WON!")
         break
     elif board[1] == board[4] == board[7] != " ":
         print(board[1] , "WON! ")
         break
     elif board[2] == board[5] == board[8] != " ":
         print(board[2] , "WON! ")
         break
     elif board[0] == board[4] == board[8] != " ":
         print(board[0] , "WON! ")
         break
     elif board[2] == board[4] == board[6] != " ":
         print(board[6] , "WON! ")
         break
     elif count > 9 :
          print("It is a tie")  