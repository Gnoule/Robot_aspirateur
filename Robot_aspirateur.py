class Aspirateur:
    def __init__(self, x, y, orientation): #initialisation des variables
        self.x = x
        self.y = y
        self.orientation = orientation
        self.directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    def movement(self): #Création de la def pour les mouvements de l'aspirateur
        dx, dy = self.directions[self.orientation] #Stockage dans les variables 
        self.x += dx
        self.y += dy

        
    def turn(self, index): #Création de la def pour la rotation de l'aspirateur
        orientations = list('NESW')
        current_orientation_index = orientations.index(self.orientation) # Récupration de l'orientation actuelle
        new_orientation_index = (current_orientation_index + index) % 4 # Création de la nouvelle orientation à l'aide du modulo
        self.orientation = orientations[new_orientation_index]
            
    def execute(self, command): #Création de la def qui execute le programme
        if command == 'A': # Condition if pour savoir quelle def utiliser en fonction de l'input utilisateur
            self.movement()
        elif command == 'G':
            self.turn(1)
        elif command == 'D':
            self.turn(-1)

def main(): #Création de la fonction main
    grid_x, grid_y = map(int, input().split()) #Récuperation de la taille de la maps à l'aide de la fonction split
    x, y, orientation = input().split() #Récuperation de l'orietation de depart à l'aide de la fonction split
    x, y = int(x), int(y) #transformation en int

    aspirateur = Aspirateur(x, y, orientation) #Appliation pour le choix de l'input
    commands = input()
    for command in commands:
        aspirateur.execute(command)

    print(f"la position finale de l'aspirateur est': {aspirateur.x}, {aspirateur.y}, {aspirateur.orientation}")


main()