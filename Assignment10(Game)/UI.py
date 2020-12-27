class Console():
    
    def __init__(self,service):
        self.__service=service
    def __uiCreateBoard(self,parameters):
        dimensions=parameters[0]
        self.__service.createBoard(dimensions)
    
    def __uiDisplayBoard(self,parameters):
        print(" ")
        board=self.__service.getBoard()
        dimensions=len(board)
        for lines in board:
            index=0
            while(index<dimensions):
                print(lines[index], end=' ')
                index+=1
            print("\n")
        
    def __uiPlanMove(self,parameters):
        line_position=int(parameters[0])
        column_position=int(parameters[1])
        self.__service.planMove(line_position,column_position) 
        status_game=self.__service.status_game()
        if status_game!=0:
            self.__service.computerMove()
            next_status_game=self.__service.status_game()
            if next_status_game==0:
                raise Exception("Computer won!")
        else:
            raise Exception("You won!")
        print(" ")
        self.__uiDisplayBoard(self)
    
    def instructions_menu(self): 
        print("In this game you can identify yourself with the sign X and the computer with O")
        print("You are allowed to use commands like:")
        print(" --> create <dimensions> - with this command you create the board of the game with the dimensions you prefer")
        print(" --> display - displays on the screen the board game")
        print(" --> choose <line_position> <column_position> - with this command you put X wherever you please ; the position starts from value 0")
        print(" --> exit - stops the game")
        print("Good luck ! :)")
        print("")
    def run(self):
        functions={"create":self.__uiCreateBoard,
                   "display": self.__uiDisplayBoard,
                   "choose": self.__uiPlanMove}
        self.instructions_menu()        
        while(True):
            command=str(input("Use one command from those mentioned above:"))
            if command=="exit":
                break
            parameters=command.split()
            try:
                functions[parameters[0]](parameters[1:])
            except Exception as ex:
                    print(ex)