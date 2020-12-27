class GameRepo():
    def __init__(self):
        self._board_game=[]
        self._board_left=[]
        self._spaces_left=0
    def createBoard(self,dimensions):
        firstIndex=0
        while(firstIndex<dimensions):
            one_line_board_game=[]
            one_line_board_left=[]
            secondIndex=0
            while(secondIndex<dimensions):
                one_line_board_game.append('*')
                one_line_board_left.append(0)
                secondIndex+=1
            self._board_game.append(one_line_board_game)
            self._board_left.append(one_line_board_left)
            firstIndex+=1
        self._spaces_left=dimensions*dimensions
       
    def addMove(self,move):
        del self._board_game[int(move.get_line_position())][int(move.get_column_position())]
        self._board_game[int(move.get_line_position())].insert(int(move.get_column_position()),move)
        
    def calculateBoardAreaLeft(self,line_position,column_position):
        if(self._board_left[line_position][column_position]==0):
            self._board_left[line_position][column_position]=1
            self._spaces_left-=1
            
    def getBoard(self):
        return self._board_game[:]
    
    
    def getSpacesLeft(self):
        return self._spaces_left

