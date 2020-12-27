from Domain.domains import X,O
import random
class GameService():
    def __init__(self,gameValidators,gameRepo):
        self.__gameValidators = gameValidators
        self.__gameRepo = gameRepo
    
    def createBoard(self,dimensions):
        board=self.__gameRepo.getBoard()
        if(len(board)==0):
            self.__gameRepo.createBoard(int(dimensions))
        else:
            raise Exception("The board game was already created!")
    
    def computerMove(self):
        board=self.__gameRepo.getBoard()
        possible_position_values=[]
        for i in range(0,len(board)):
            possible_position_values.append(i)
        while(True):
            board=self.__gameRepo.getBoard()
            line_position=random.choice(possible_position_values)
            column_position=random.choice(possible_position_values)
            if(board[line_position][column_position]=='*'):
                if (line_position==0 and column_position==len(board)-1):
                    if board[line_position][column_position-1]=='*' and board[line_position+1][column_position-1]=='*' and board[line_position+1][column_position]=='*':
                        computer_move=O(line_position,column_position,"O")
                        self.__gameRepo.addMove(computer_move)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position-1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
                        break
                elif (line_position==0 and column_position!=0 and column_position!=len(board)-1):
                    if board[line_position][column_position-1]=='*' and board[line_position][column_position+1]=='*' and board[line_position+1][column_position+1]=='*' and board[line_position+1][column_position-1]=='*' and board[line_position+1][column_position]=='*': 
                        computer_move=O(line_position,column_position,"O")
                        self.__gameRepo.addMove(computer_move)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position+1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position-1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
                        break
                elif (line_position==0 and column_position==0):
                    if board[line_position][column_position+1]=='*' and board[line_position+1][column_position+1]=='*' and board[line_position+1][column_position]=='*':
                        computer_move=O(line_position,column_position,"O")
                        self.__gameRepo.addMove(computer_move)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position+1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
                        break
                elif (column_position==0 and line_position==len(board)-1):
                    if board[line_position-1][column_position]=='*' and board[line_position-1][column_position+1]=='*' and board[line_position][column_position+1]=='*': 
                        computer_move=O(line_position,column_position,"O")
                        self.__gameRepo.addMove(computer_move)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position+1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
                        break
                
                elif (column_position==0 and line_position!=0 and line_position!=len(board)-1):
                    if board[line_position-1][column_position]=='*' and board[line_position+1][column_position]=='*' and board[line_position-1][column_position+1]=='*' and board[line_position][column_position+1]=='*' and board[line_position+1][column_position+1]=="*":
                        computer_move=O(line_position,column_position,"O")
                        self.__gameRepo.addMove(computer_move) 
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)   
                        self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position+1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position+1)
                        break
                    
                elif(line_position==len(board)-1 and column_position==len(board)-1):
                    if board[line_position-1][column_position]=='*' and board[line_position-1][column_position-1]=='*' and board[line_position][column_position-1]=='*': 
                        computer_move=O(line_position,column_position,"O")
                        self.__gameRepo.addMove(computer_move)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position-1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
                        break
                elif(line_position==len(board)-1 and column_position!=0 and column_position!=len(board)-1):
                    if board[line_position][column_position-1]=='*' and board[line_position][column_position+1]=='*' and board[line_position-1][column_position-1]=='*' and board[line_position-1][column_position]=='*' and board[line_position-1][column_position+1]=="*":
                        computer_move=O(line_position,column_position,"O")
                        self.__gameRepo.addMove(computer_move)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position-1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position+1)
                        break 
                    
                elif(line_position!=0 and line_position!=len(board)-1 and column_position==len(board)-1):
                    if board[line_position-1][column_position]=='*' and board[line_position+1][column_position]=='*' and board[line_position][column_position-1]=='*' and board[line_position-1][column_position-1]=='*' and board[line_position+1][column_position-1]=='*':
                        computer_move=O(line_position,column_position,"O")
                        self.__gameRepo.addMove(computer_move)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
                        self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position-1)
                        self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position-1)
                        break
        
                elif board[line_position-1][column_position]=='*' and board[line_position+1][column_position]=='*' and board[line_position][column_position+1]=='*' and board[line_position][column_position-1]=='*' and board[line_position-1][column_position-1]=='*' and board[line_position-1][column_position+1]=='*' and board[line_position+1][column_position-1]=='*' and board[line_position+1][column_position+1]=='*': 
                    computer_move=O(line_position,column_position,"O")
                    self.__gameRepo.addMove(computer_move)
                    self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                    self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
                    self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
                    self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
                    self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
                    self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position-1)
                    self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position+1)
                    self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position-1)
                    self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position+1)
                    break
        
    def planMove(self,line_position,column_position):
        board=self.__gameRepo.getBoard()
        if(line_position>=len(board) or line_position<0 or column_position>=len(board) or column_position<0):
            raise Exception("Invalid move! Try again!")
        step_done=False
        if (line_position==0 and column_position==len(board)-1):
            if board[line_position][column_position-1]=='*' and board[line_position+1][column_position-1]=='*' and board[line_position+1][column_position]=='*':
                player_move=X(line_position,column_position,"X")
                self.__gameRepo.addMove(player_move)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
                self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position-1)
                self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
                step_done=True
        elif (line_position==0 and column_position!=0 and column_position!=len(board)-1):
            if board[line_position][column_position-1]=='*' and board[line_position][column_position+1]=='*' and board[line_position+1][column_position+1]=='*' and board[line_position+1][column_position-1]=='*' and board[line_position+1][column_position]=='*': 
                player_move=X(line_position,column_position,"X")
                self.__gameRepo.addMove(player_move)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
                self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position+1)
                self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position-1)
                self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
                step_done=True
        elif (line_position==0 and column_position==0):
            if board[line_position][column_position+1]=='*' and board[line_position+1][column_position+1]=='*' and board[line_position+1][column_position]=='*':
                player_move=X(line_position,column_position,"X")
                self.__gameRepo.addMove(player_move)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
                self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position+1)
                self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
                step_done=True
        elif (column_position==0 and line_position==len(board)-1):
            if board[line_position-1][column_position]=='*' and board[line_position-1][column_position+1]=='*' and board[line_position][column_position+1]=='*': 
                player_move=X(line_position,column_position,"X")
                self.__gameRepo.addMove(player_move)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position+1)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
                step_done=True
        elif (column_position==0 and line_position!=0 and line_position!=len(board)-1):
            if board[line_position-1][column_position]=='*' and board[line_position+1][column_position]=='*' and board[line_position-1][column_position+1]=='*' and board[line_position][column_position+1]=='*' and board[line_position+1][column_position+1]=="*":
                player_move=X(line_position,column_position,"X")
                self.__gameRepo.addMove(player_move) 
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)   
                self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position+1)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
                self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position+1)
                step_done=True
        elif(line_position==len(board)-1 and column_position==len(board)-1):
            if board[line_position-1][column_position]=='*' and board[line_position-1][column_position-1]=='*' and board[line_position][column_position-1]=='*': 
                player_move=O(line_position,column_position,"X")
                self.__gameRepo.addMove(player_move)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position-1)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
                step_done=True
                
        elif(line_position==len(board)-1 and column_position!=0 and column_position!=len(board)-1):
            if board[line_position][column_position-1]=='*' and board[line_position][column_position+1]=='*' and board[line_position-1][column_position-1]=='*' and board[line_position-1][column_position]=='*' and board[line_position-1][column_position+1]=="*":
                player_move=X(line_position,column_position,"X")
                self.__gameRepo.addMove(player_move)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
                self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position-1)
                self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position+1)
                step_done=True
        elif(line_position!=0 and line_position!=len(board)-1 and column_position==len(board)-1):
            if board[line_position-1][column_position]=='*' and board[line_position+1][column_position]=='*' and board[line_position][column_position-1]=='*' and board[line_position-1][column_position-1]=='*' and board[line_position+1][column_position-1]=='*':
                player_move=X(line_position,column_position,"X")
                self.__gameRepo.addMove(player_move)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
                self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
                self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position-1)
                self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position-1)
                step_done=True
        elif board[line_position-1][column_position]=='*' and board[line_position+1][column_position]=='*' and board[line_position][column_position+1]=='*' and board[line_position][column_position-1]=='*' and board[line_position-1][column_position-1]=='*' and board[line_position-1][column_position+1]=='*' and board[line_position+1][column_position-1]=='*' and board[line_position+1][column_position+1]=='*': 
            player_move=X(line_position,column_position,"X")
            self.__gameRepo.addMove(player_move)
            self.__gameRepo.calculateBoardAreaLeft(line_position,column_position)
            self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position)
            self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position)
            self.__gameRepo.calculateBoardAreaLeft(line_position,column_position+1)
            self.__gameRepo.calculateBoardAreaLeft(line_position,column_position-1)
            self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position-1)
            self.__gameRepo.calculateBoardAreaLeft(line_position-1,column_position+1)
            self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position-1)
            self.__gameRepo.calculateBoardAreaLeft(line_position+1,column_position+1)
            step_done=True
        
        if(step_done==False):
            raise Exception("Invalid move! Try again!")
    
    def status_game(self): 
        return self.__gameRepo.getSpacesLeft() 
          
    def getBoard(self):
        board=self.__gameRepo.getBoard()
        return board