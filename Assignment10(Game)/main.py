from Interface.UI import Console
from Service.Service import GameService
from Validators.Validator import GameValidators
from Repository.Repository import GameRepo
gameValidators=GameValidators()
gameRepo=GameRepo()
gameService=GameService(gameValidators,gameRepo)
ui=Console(gameService)
ui.run()