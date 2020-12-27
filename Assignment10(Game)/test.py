import unittest
from Service.Service import GameService
from Repository.Repository import GameRepo
from Validators.Validator import GameValidators
from Domain.domains import X,O
class UnitTesting(unittest.TestCase):
    
    def testCreationOfEntityX_validLinePosition_linePositionCorrectlyAddedToEntityX(self):
        player_move=X(1,1,"X")
        self.assertEqual(player_move.get_line_position(), 1, "Incorrect line position!")
        
    def testCreationOfEntityX_validColumnPosition_columnPositionCorrectlyAddedToEntityX(self):
        player_move=X(2,2,"X")
        self.assertEqual(player_move.get_column_position(), 2, "Incorrect column position!")
        
    def testCreationOfEntityX_validRepresentation_representationCorrectlyAddedToEntityX(self):
        player_move=X(3,3,"X")
        self.assertEqual(player_move.get_representation(), "X", "Incorrect representation!")
        
    def testCreationOfEntityO_validLinePosition_linePositionCorrectlyAddedToEntityO(self):
        computer_move=O(3,2,"O")
        self.assertEqual(computer_move.get_line_position(), 3, "Incorrect line position!")
        
    def testCreationOfEntityO_validColumnPosition_columnPositionCorrectlyAddedToEntityO(self):
        computer_move=O(4,5,"O")
        self.assertEqual(computer_move.get_column_position(), 5, "Incorrect column position!")
        
    def testCreationOfEntityO_validRepresentation_representationCorrectlyAddedToEntityO(self):
        computer_move=O(2,5,"O")
        self.assertEqual(computer_move.get_representation(), "O", "Incorrect representation!")
        
    def testCreateBoard_validDimensions_boardSuccesfullyCreated(self):
        gameRepo=GameRepo()
        gameValidators=GameValidators()
        gameService=GameService(gameValidators,gameRepo)
        gameService.createBoard(3)
        board=gameService.getBoard()
        self.assertEqual(len(board), 3, "Error board creation!")
        gameRepo._board_game.clear()
        gameRepo._board_left.clear()
        gameRepo._spaces_left=0
        
    def testComputerMove_noInput_computerChooseAValidMove(self):
        gameRepo=GameRepo()
        gameValidators=GameValidators()
        gameService=GameService(gameValidators,gameRepo)
        gameService.createBoard(3)
        gameService.computerMove()
        board=gameService.getBoard()
        existence_move=False
        for i in range(0,len(board)):
            for j in range(0,len(board)):
                if(board[i][j]!="*"):
                    if(board[i][j].get_representation()=="O"):
                        existence_move=True
        self.assertEqual(existence_move, True, "Invalid move!")
        gameRepo._board_game.clear()
        gameRepo._board_left.clear()
        gameRepo._spaces_left=0
        
    def testPlayerMove_validMove_moveSuccesfullyAddedOnTheBoard(self):
        gameRepo=GameRepo()
        gameValidators=GameValidators()
        gameService=GameService(gameValidators,gameRepo)
        gameService.createBoard(3)
        gameService.planMove(1, 2)
        board=gameService.getBoard()
        self.assertEqual(board[1][2].get_representation(),"X", "Invalid move!")
        gameRepo._board_game.clear()
        gameRepo._board_left.clear()
        gameRepo._spaces_left=0
        
    def testCalculateAreaLeft_validMove_newAreaLeftSuccesfullyCalculated(self):
        gameRepo=GameRepo()
        gameValidators=GameValidators()
        gameService=GameService(gameValidators,gameRepo)
        gameService.createBoard(3)
        gameService.planMove(1, 1)
        boardAreaLeft=gameService.status_game()
        self.assertEqual(boardAreaLeft, 0, "Board area incorrectly calculated!")
        gameRepo._board_game.clear()
        gameRepo._board_left.clear()
        gameRepo._spaces_left=0
        