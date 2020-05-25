import constants
import copy
import random

if __name__ == '__main__':

    teams = copy.deepcopy(constants.TEAMS)
    players = copy.deepcopy(constants.PLAYERS)
    
    experienced = []
    inexperienced = []
    
    panthers = []
    bandits = []
    warriors = []
    
    def clean_data():
        for player in players:
            player['guardians'] = player['guardians'].split(" and ")
            player['height'] = int(player['height'][:2])
            if player['experience'] == "YES":
                player['experience'] = True
                experienced.append(player)
            else:
                player['experience'] = False
                inexperienced.append(player)
    
    
    clean_data()            
                
    #Count the number of Teams and Players
    no_of_teams = len(teams)
    no_of_players = len(players)
    players_per_team = int(no_of_players / no_of_teams)
    
    
    #Count the number of Inexperienced and Experienced Players
    no_of_inexperienced = len(inexperienced)
    no_of_experienced = len(experienced)
    inexp_per_team = int(no_of_inexperienced / no_of_teams)
    exp_per_team = int(no_of_experienced / no_of_teams)
    
    #Team Balancing Operation
    def team_balancing(team):
        exp_counter = 0
        while exp_counter < exp_per_team:
             team.append(experienced.pop(random.randrange(len(experienced))))
             exp_counter += 1
        inexp_counter = 0
        while inexp_counter < inexp_per_team:
            team.append(inexperienced.pop(random.randrange(len(inexperienced))))
            inexp_counter += 1
        amount_of_players = len(team)
    
    #Balance all 3 teams.
    team_balancing(panthers)
    team_balancing(bandits)
    team_balancing(warriors)
    
    #Main Output Master
    def team_master(team):
        #Player Names
        player_names = []
        for player in team:
            player_names.append(player['name'])
        print("Player Names: ", ", ".join(player_names))
        
        #Number of Players
        amount_of_players = 0
        for player in team:
            amount_of_players += 1
        print("Number of Players: ", amount_of_players)
        
        #Number of Experienced Players
        amount_of_exp = 0
        for player in team:
            if player['experience']:
                amount_of_exp += 1
        print("Number of Experienced Players: ", amount_of_exp)
        
        #Number of Inexperienced Players
        amount_of_inexp = 0
        for player in team:
            if player['experience']:
                amount_of_inexp += 1
        print("Number of Inxperienced Players: ", amount_of_inexp)
        
        #Average Height
        total_height = 0
        for player in team:
            total_height += player['height']
        average_height = float(total_height / amount_of_players)
        print("Average Height of Players: {0:.2f}".format(average_height))
        
        #Player Guardians
        player_guardians = []
        for player in team:
            player_guardians.extend(player['guardians'])
        print("Guardians: ", ", ".join(player_guardians))    
    
    #The game itself!    
    def the_game():
        print("Welcome to the Basketball Stats Team Tool, Developed by Johnny Austen.\n\n --- MENU ---\n")
        while True:
            try:
                initial_choice = int(input("Please select from the following choices: \n 1) View Team Stats \n 2) End Session / Quit \n"))
            
                if initial_choice == 2:
                    print("Thanks for visiting! Have a great day.")
                    break
                elif initial_choice > 2:
                    print("Sorry, the number you selected is too high. Please try again.\n")
                    continue
                elif initial_choice < 1:
                    print("Sorry, the number you selected is too low. Please try again.\n")
                    continue
                
                elif initial_choice == 1:
                    start_game = True
                    while start_game == True:
                            team_selection = input("\n Please select from the following teams: \n 1) Panthers \n 2) Bandits \n 3) Warriors \n 4) Return to Main Menu. ")
                            if  team_selection == '5':
                                print("Oops, that number is too high! Please try again.\n")
                                start_game = True
                                continue
                            if team_selection == '1':
                                print("Team Stats: Panthers")
                                team_master(panthers)
                                start_game = True
                                continue
                            elif team_selection == '2':
                                print("Team Stats: Bandits")
                                print("**-----**")
                                team_master(bandits)
                                print("**-----**\n")
                                start_game = True
                                continue
                            elif team_selection == '3':
                                print("Team Stats: Warriors")
                                print("**-----**")
                                team_master(warriors)
                                print("**-----**\n")
                                start_game = True
                                continue
                            elif team_selection <= '0':
                                print("Oops, that number is too low! Please try again.\n")
                            elif team_selection == '4':
                                print("Return to Main Menu!\n")
                                break
                            else:
                                print("You have returned an invalid value. Please try again. \n")
                                continue
            except ValueError:
                print("Sorry, that's an invalid option.\n")
    the_game()