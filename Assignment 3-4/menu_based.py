from functions import*
import copy
def startMenuBased():
    scoreList=initialValueScores()
    undoList=[]
    undoList.append(initialValueScores())
    while True:
      modification=[]
      print_menu()
      command=int(input("Which option would you like to choose:"    , ))
      print("")
      if (command==1):
          print("")
          print_menu_add()
          command_add=int(input("Which option would you like to choose:"    , ))
          if(command_add==1):
              score1 = int(input("Type the first score:", ))
              score2 = int(input("Type the second score:", ))
              score3 = int(input("Type the third score:", ))
              add(scoreList,score1,score2,score3)
              modification = scoreList.copy()
              undoList.append(modification)
          if(command_add==2):
              score1 = int(input("Type the first score:", ))
              score2 = int(input("Type the second score:", ))
              score3 = int(input("Type the third score:", ))
              position=int(input("Type the position:", ))
              insert(scoreList,position,score1,score2,score3)
              modification = scoreList.copy()
              undoList.append(modification)
      elif (command==2):
          print("")
          displayListScore(scoreList)
      elif(command==3):
          print("")
          print_menu_change_scores()
          command_remove=int(input("Which option would you like to choose:"    , ))
          if(command_remove==1):
               print("")
               startPosition=int(input("Introduce the position from where to remove scores:", ))
               finalPosition=int(input("Introduce the position where to stop removing scores:",))
               remove(scoreList,startPosition,finalPosition)
               modification = scoreList.copy()
               undoList.append(modification)
          elif(command_remove==2):
               print("")
               position=int(input("Introduce the contestant to whom would you like to change the score:", ))
               problem=int(input("Introduce the probe at which would you like to change the score:", ))
               newScore=int(input("Introduce the new score:"))
               replace(scoreList,position,problem,newScore)
               modification = scoreList.copy()
               undoList.append(modification)
      elif(command==4):
               print("")
               print_menu_score_proprieties()
               command_list=int(input("Which option would you like to choose:"    , ))
               if(command_list==1):
                    print("")
                    List(scoreList)
                    
               elif(command_list==2):
                    print("")
                    listSorted(scoreList)
                    print(scoreList)
                    modification = scoreList.copy()
                    undoList.append(modification)
               elif(command_list==3):
                    print("")
                    print_menu_score_proprieties_3()
                    command_list_different_proprieties=int(input("Which option would you like to choose:"    , ))
                    if (command_list_different_proprieties==1):
                        print("")
                        number=int(input("Choose the number of comparation:"   , ))
                        listLessThanNumber(scoreList,number)
                    elif (command_list_different_proprieties==2):
                        print("")
                        number=int(input("Choose the number of comparation:"   , ))
                        listEqualNumber(scoreList,number)
                    elif (command_list_different_proprieties==3):
                        print("")
                        number=int(input("Choose the number of comparation:"   , ))
                        listGreaterThanNumber(scoreList,number)
      elif(command==5):
           print("")
           print_menu_characteristic_participants()
           command_different_characteristics_contestants=int(input("Which option would you like to choose:"))
           if(command_different_characteristics_contestants==1):
               startPosition=int(input("Type the first position:"))
               finalPosition=int(input("Type the second position:"))
               print(averageOfAverageListScore(scoreList,startPosition,finalPosition))
           elif(command_different_characteristics_contestants==2):
               startPosition = int(input("Type the first position:"))
               finalPosition = int(input("Type the second position:"))
               print(minimumAverageScore(scoreList,startPosition,finalPosition))
      elif (command == 6):
           print("")
           print_menu_establish_podium()
           command_podium=int(input("Which option would you like to choose:"))
           if (command_podium==1):
               number=int(input("Choose how many contestants do you want in the top:"))
               listTop(scoreList,number)
           elif(command_podium==2):
               number = int(input("Choose how many contestants do you want in the top:"))
               problem=int(input("Choose the probe"))
               listTopProbe(scoreList,number,problem)
           elif(command_podium==3):
                number = int(input("Choose the number of comparation:", ))
                removeLessThanANumber(scoreList,number)
                modification = scoreList.copy()
                undoList.append(modification)
           elif (command_podium == 4):
               number = int(input("Choose the number of comparation:", ))
               removeEqualToANumber(scoreList, number)
               modification = scoreList.copy()
               undoList.append(modification)
           elif (command_podium == 5):
               number = int(input("Choose the number of comparation:", ))
               removeGreaterThanANumber(scoreList, number)
               modification = scoreList.copy()
               undoList.append(modification)
      elif (command == 7):
            if (len(undoList))>1:
              del undoList[len(undoList)-1]
              scoreList=copy.deepcopy(undoList[len(undoList)-1])
            else:
                print("No more undo can be effectuated!")
      elif(command==8):
           break
      else:
          print("Invalid command!")
      print("")

