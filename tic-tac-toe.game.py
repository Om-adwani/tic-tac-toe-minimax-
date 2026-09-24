import copy
import time 
count=0
def display_board(p):
    n=len(p)
    for i in p:
      a=",".join(i)
      print(a.replace(","," | "))
      n-=1
      if n!=0:
        print("----------")
def win(board):
  n=len(board)
  line=[]
  line.extend(board)
  for i in range(n):
    line.append([board[j][i] for j in range(n)])
  line.append([board[j][j] for j in range(n)])
  line.append([board[j][n-1-j] for j in range(n)])
  for p in line:
    first=p[0]
    if first!=" " and all(k==first for k in p):
      return "winner",first
  for i in board:
    if i.count(" ")!=0:
      return None
  else:
      return "tie","draw"  

def get_available_move(d):
   free_move=[]
   n=len(d)
   for i in range(n):
     for j in range(n):
        if d[i][j]==" ":
          free_move.append((i,j))
   return free_move
def make_move(d,position,player):
  for i in range(len(d)):
    for j in range(len(d)):
      if (i,j)==position:
        d[i][j]=player
  return d
def score(d):
   u=win(d)
   if u==None:
     return None
   elif u[1].lower()=="o":
    return 1
   elif u[1].lower()=="x":
    return -1
   elif u[1].lower()=="draw":
    return 0
def minimax(d,player,alpha,beta):
   global count
   count+=1
   result=score(d)
   if result is not None:
    return result
   else:
     moves=get_available_move(d)
     best_score_max=-1
     best_score_min=1
     for i,j in moves:
       d=make_move(d,(i,j),player)
       if player=="x":
         current_score=minimax(d,"o",alpha,beta)
         if current_score<best_score_min:
           best_score_min=current_score
           beta = current_score
       elif player=="o":
         current_score=minimax(d,"x",alpha,beta)
         if current_score>best_score_max:
           best_score_max=current_score
           alpha = current_score
       d[i][j]=" "
       if alpha>=beta:
                break 
     if player=="x":
      return best_score_min
     else:
      return best_score_max    
def best_move(board,player):
    best_score=-1
    best_position=""
    moves=get_available_move(board)
    if player=="x":
      opponent="o"
    else:
      opponent="x"
    for i in moves:
      virtual_game=copy.deepcopy(board)
      make_move(virtual_game,i,player)
      current_score=minimax(virtual_game,opponent,float("-inf"),float("inf"))
      if current_score>best_score:
        best_score=current_score
        best_position=i
    return best_position
d=[[" "]*3,[" "]*3,[" "]*3]
display_board(d)
while True:
  make_move_human_x,make_move_human_y=input("it,s your turn:").split(",")
  d[int(make_move_human_x)][int(make_move_human_y)]="x"
  display_board(d)
  print(best_move(d,"o"))
  if win(d)==None:
     x=best_move(d,"o")
     make_move(d,x,"o")
     display_board(d)
     if win(d)==("winner","o") or win(d)==("tie","draw"): 
       break
  elif win(d)[0]=="winner":
     i,j=win(d)
     print(i,j)
     break
  elif win(d)[0]=="tie":
     print("draw")
     break
start = time.perf_counter()
x = best_move(d, "o")
end = time.perf_counter()
print("Time:", end - start)
print(count)