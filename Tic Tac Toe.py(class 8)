
#Tic Tac Toe

board=["1","2","3",
       "4","5","6",
       "7","8","9" ]
current_player="X"
game_over=False
print("Welcome to Tic Tac Toe")
print("Choose a position between 1-9")
while game_over==False:
  print(" "+board[0]+" | "+board[1]+" | "+board[2])
  print("---|---|---")
  print(" "+board[3]+" | "+board[4]+" | "+board[5])
  print("---|---|---")
  print(" "+board[6]+" | "+board[7]+" | "+board[8])
  position=int(input("Player "+current_player+" Enter your position "))
  #check valid position
  if position<1 or position>9:
    print("invalid move")
  #Check if position is already filled
  elif board[position-1]=="X" or board[position-1]=="O":
    print("This Position is already filled")
  else:
    board[position-1]=current_player
  #check horizontal winning combination
  if(board[0]==board[1]==board[2] or
     board[3]==board[4]==board[5] or
     board[6]==board[7]==board[8]):
    game_over=True
  #check vertical winning combination
  if(board[0]==board[3]==board[6] or
     board[1]==board[4]==board[7] or
     board[2]==board[5]==board[8]):
      game_over=True
   #check diagonal winning combination
  if(board[0]==board[4]==board[8] or
     board[2]==board[4]==board[6]):
      game_over=True
  #win check
  if game_over==True:
    print(" "+board[0]+" | "+board[1]+" | "+board[2])
    print("---|---|---")
    print(" "+board[3]+" | "+board[4]+" | "+board[5])
    print("---|---|---")
    print(" "+board[6]+" | "+board[7]+" | "+board[8])
    
    print("Player "+current_player+" wins!")
  #draw check
  elif all(cell=="X" or cell=="O" for cell in board):
    print("It's a draw!")
    game_over=True
    
  #Change player
  else:
    if current_player=="X":
      current_player="O"
    else:
      current_player="X"
