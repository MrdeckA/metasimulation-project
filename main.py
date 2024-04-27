
# Question 1 : Proposer une structure de données qui permet de représenter le programme d’une RAM.

class RAMProgram:
    def __init__(self):
        self.instructions = []  # Liste des instructions de la RAM

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def remove_instruction(self, index):
        del self.instructions[index]

    def clear_program(self):
        self.instructions = []

    def get_instruction(self, index):
        return self.instructions[index]

    def __len__(self):
        return len(self.instructions)
    
    def __str__(self):
        program_str = ""
        for index, instruction in enumerate(self.instructions):
            program_str += f"Instruction {index + 1}: {instruction}\n"
        return program_str


class RAMInstruction:
    def __init__(self, op, args):
        self.op = op  # Opération (ex: ADD, SUB, JUMP)
        self.args = args  # Liste des arguments de l'instruction

    def __str__(self):
        return f"{self.op}({' '.join(map(str, self.args))})"



# Test Question 1
# Création d'un programme RAM
program = RAMProgram()

# Ajout d'instructions au programme
program.add_instruction(RAMInstruction("ADD", [1, 2, 3]))
program.add_instruction(RAMInstruction("SUB", [4, 5, 6]))

# Affichage du programme
for index, instruction in enumerate(program.instructions):
    print(f"Instruction {index + 1}: {instruction}")

# Suppression d'une instruction
program.remove_instruction(0)

# Affichage du programme mis à jour
for index, instruction in enumerate(program.instructions):
    print(f"Instruction {index + 1}: {instruction}")



# Suite Question 1 : Ecrire une fonction qui lit un fichier texte contenant le code d’une machine RAM et un mot d’entrée et qui initialise la structure de données pour représenter cette machine. Vous pourrez éventuellement utiliser lex et yacc pour cette question.
def initialize_RAM_from_file(file_path, input_word):
    program = RAMProgram()  # Initialisation d'un programme RAM vide
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Lire les lignes du fichier
        for line in lines:
            line = line.strip()  # Supprimer les espaces en début et fin de ligne
            if line:  # Ignorer les lignes vides
                # Ajouter l'instruction au programme
                instruction_parts = line.split()  # Séparer l'instruction en parties
                operation = instruction_parts[0]  # Première partie : opération
                args = [int(arg) if arg.isdigit() else arg for arg in instruction_parts[1:]]  # Autres parties : arguments
                program.add_instruction(RAMInstruction(operation, args))

    # Initialiser les registres d'entrée avec le mot d'entrée
    input_size = len(input_word)
    program.add_instruction(RAMInstruction("ADD", [0, input_size, 0]))  # Mettre la taille du mot d'entrée dans i0
    for i, char in enumerate(input_word, start=1):
        program.add_instruction(RAMInstruction("ADD", [i, ord(char), 0]))  # Remplir les registres d'entrée

    return program

# Exemple d'utilisation :
file_path = "file.txt"
input_word = "example"
program = initialize_RAM_from_file(file_path, input_word)
print("\n")
print(program)




# Question 2 : Proposer une structure de données pour représenter une configuration d’une Machine RAM.
class RAMConfiguration:
    def __init__(self, pos, registers):
        self.pos = pos  # Position du pointeur de code
        self.registers = registers  # Valeurs des registres

    def update_register(self, reg_num, value):
        self.registers[reg_num] = value

    def get_register_value(self, reg_num):
        return self.registers[reg_num]

    def __str__(self):
        return f"Position du pointeur de code : {self.pos}\n" + \
               f"Valeurs des registres : {self.registers}"
               
               

# Exemple d'utilisation :
pos = 0  # Position initiale du pointeur de code
registers = [0] * 10  # Initialisation des registres à zéro
config = RAMConfiguration(pos, registers)

# Mise à jour d'un registre
config.update_register(1, 5)

# Obtention de la valeur d'un registre
print(config.get_register_value(1))

# Affichage de la configuration
print(config)



# Suite Question 2 : Donner une fonction qui prend en argument une machine RAM et une configuration et qui donne la configuration obtenue après un pas de calcul de la machine
def execute_RAM_instruction(machine, config):
    # Récupérer l'instruction à exécuter
    instruction = machine.get_instruction(config.pos)
    op = instruction.op
    args = instruction.args

    # Exécuter l'instruction
    if op == "ADD":
        reg1, reg2, reg3 = args
        config.registers[reg3] = config.registers[reg1] + config.registers[reg2]
        config.pos += 1
    elif op == "SUB":
        reg1, reg2, reg3 = args
        config.registers[reg3] = config.registers[reg1] - config.registers[reg2]
        config.pos += 1
    elif op == "MULT":
        reg1, reg2, reg3 = args
        config.registers[reg3] = config.registers[reg1] * config.registers[reg2]
        config.pos += 1
    elif op == "DIV":
        reg1, reg2, reg3 = args
        config.registers[reg3] = config.registers[reg1] // config.registers[reg2]
        config.pos += 1
    elif op == "JUMP":
        z = args[0]
        config.pos += z
    elif op == "JE":
        reg1, reg2, z = args
        if config.registers[reg1] == config.registers[reg2]:
            config.pos += z
        else:
            config.pos += 1
    elif op == "JL":
        reg1, reg2, z = args
        if config.registers[reg1] < config.registers[reg2]:
            config.pos += z
        else:
            config.pos += 1

    return config

# Définir une machine RAM simple
machine = RAMProgram()
machine.add_instruction(RAMInstruction("ADD", [1, 2, 3]))  # ADD(r1, r2, r3)
machine.add_instruction(RAMInstruction("SUB", [3, 1, 4]))  # SUB(r3, r1, r4)
machine.add_instruction(RAMInstruction("JUMP", [2]))       # JUMP(2)

# Définir une configuration initiale
initial_config = RAMConfiguration(0, [0, 10, 5, 0, 0])

# Exécuter chaque instruction et afficher la configuration après chaque pas
for i in range(3):
    print(f"Avant l'exécution de l'instruction {i+1}:")
    print(initial_config)
    print("---------------")
    initial_config = execute_RAM_instruction(machine, initial_config)
    print(f"Après l'exécution de l'instruction {i+1}:")
    print(initial_config)
    print("---------------\n")




# Question 3 : Ecrire une fonction qui prend comme argument un mot et une machine RAM et qui simule le calcul de la machine sur le mot jusqu’à atteindre l’état final. Bravo, vous avez réalisé une machine universelle
def simulate_RAM_machine(word, machine):
    # Initialisation de la configuration
    input_size = len(word)
    config = RAMConfiguration(0, [input_size] + [ord(char) for char in word] + [0] * (len(machine) - input_size - 1))

    # Boucle de simulation
    while config.pos < len(machine):
        config = execute_RAM_instruction(machine, config)

    # Récupération du mot de sortie
    output_size = config.registers[0]
    output_word = ''.join(chr(config.registers[i]) for i in range(1, output_size + 1))

    return output_word

# Exemple d'utilisation :
# Supposons que "machine" est une instance de RAMProgram et "word" est un mot d'entrée
word = "example"
output_word = simulate_RAM_machine(word, machine)
print("Mot de sortie calculé par la machine RAM:", output_word)




# Question 4 : Modifier la fonction précédente pour que, à chaque pas de simulation, la configuration de la machine s’affiche de manière compréhensible (soit graphiquement, soit sur le terminal).
class RAMConfiguration:
    def __init__(self, pos, registers):
        self.pos = pos  # Position du pointeur de code
        self.registers = registers  # Valeurs des registres

    def update_register(self, reg_num, value):
        self.registers[reg_num] = value

    def get_register_value(self, reg_num):
        return self.registers[reg_num]

    def display(self):
        # Affichage des valeurs des registres
        print("Valeurs des registres : ", self.registers)
        # Affichage de la position du pointeur de code
        print("Position du pointeur de code : ", self.pos)
        print("\n")
        
        
        
def simulate_RAM_machine(word, machine):
    # Initialisation de la configuration
    input_size = len(word)
    config = RAMConfiguration(0, [input_size] + [ord(char) for char in word] + [0] * (len(machine) - input_size - 1))

    # Affichage de la configuration initiale
    print("Configuration initiale :")
    config.display()

    # Boucle de simulation
    while config.pos < len(machine):
        config = execute_RAM_instruction(machine, config)
        # Affichage de la configuration après chaque pas de simulation
        print("Après l'exécution de l'instruction :")
        config.display()

    # Récupération du mot de sortie
    output_size = config.registers[0]
    output_word = ''.join(chr(config.registers[i]) for i in range(1, output_size + 1))

    return output_word



# Exemple d'utilisation :
# Supposons que "machine" est une instance de RAMProgram et "word" est un mot d'entrée
output_word = simulate_RAM_machine(word, machine)
print("Mot de sortie calculé par la machine RAM:", output_word)



# Question 5 : Donner le code des machines de RAM suivantes : Avec en entrée deux entiers a et b, calculer ab
machine_produit = RAMProgram()
machine_produit.add_instruction(RAMInstruction("MULT", [1, 2, 3]))  # MULTIPLICATION (a * b)
machine_produit.add_instruction(RAMInstruction("JUMP", [1]))       # SAUTER À LA FIN DU PROGRAMME

config = RAMConfiguration(0, [0, 3, 5, 0, 0])  # Position du pointeur de code à 0, a = 3, b = 5, autres registres à zéro

print("Avant l'exécution de la machine RAM :")
config.display()
print("---------------")
while config.pos < len(machine_produit.instructions):
    config = execute_RAM_instruction(machine_produit, config)
    config.pos += 1  # Mise à jour de la position du pointeur de code
print("Après l'exécution de la machine RAM :")
config.display()



# Question 5 suite :  Donner le code des machines de RAM suivantes : Avec comme entrée un tableau d’entier, écrire le tableau trié dans la sortie (par un tri à bulle)
# Définition de la machine RAM pour le tri à bulle
machine_tri = RAMProgram()
machine_tri.add_instruction(RAMInstruction("ADD", [0, 0, 1]))           # Initialiser i à 0
machine_tri.add_instruction(RAMInstruction("JUMP", [10]))               # Sauter à l'étape 10
machine_tri.add_instruction(RAMInstruction("ADD", [1, 0, 4]))           # Initialiser j à 0
machine_tri.add_instruction(RAMInstruction("ADD", [5, 0, 6]))           # Initialiser swapped à 0
machine_tri.add_instruction(RAMInstruction("JUMP", [6]))                # Sauter à l'étape 6
machine_tri.add_instruction(RAMInstruction("SUB", [5, 1, 7]))           # Calculer l'indice suivant
machine_tri.add_instruction(RAMInstruction("JE", [7, 1, 2]))            # Si j = i, passer à l'étape 2
machine_tri.add_instruction(RAMInstruction("ADD", [7, 1, 8]))           # Échanger les éléments j et j+1 si nécessaire
machine_tri.add_instruction(RAMInstruction("JE", [7, 1, 3]))            # Si tab[j] <= tab[j+1], passer à l'étape 3
machine_tri.add_instruction(RAMInstruction("ADD", [6, 1, 6]))           # Sinon, marquer que l'échange a eu lieu
machine_tri.add_instruction(RAMInstruction("JUMP", [-4]))               # Recommencer la boucle interne
machine_tri.add_instruction(RAMInstruction("ADD", [4, 1, 4]))           # Incrémenter j
machine_tri.add_instruction(RAMInstruction("JE", [4, 3, -9]))           # Si j < n - i - 1, recommencer la boucle interne
machine_tri.add_instruction(RAMInstruction("ADD", [0, 1, 0]))           # Incrémenter i
machine_tri.add_instruction(RAMInstruction("JE", [0, 2, -14]))          # Si i < n - 1, recommencer la boucle externe
machine_tri.add_instruction(RAMInstruction("ADD", [3, 0, 3]))           # Stocker la taille du tableau dans o0
machine_tri.add_instruction(RAMInstruction("JUMP", [1]))                # Retourner au début du programme

# Tableau d'entrée
input_array = [5, 2, 9, 1, 6]

# Initialisation des registres
registers = [0, len(input_array)] + input_array + [0] * (len(machine_tri) - len(input_array) - 2)

# Configuration initiale
config_tri = RAMConfiguration(0, registers)

print("Avant l'exécution du tri à bulle :")
config_tri.display()
print("---------------")

while config_tri.pos < len(machine_tri.instructions):
    config_tri = execute_RAM_instruction(machine_tri, config_tri)
    config_tri.pos += 1  # Mise à jour de la position du pointeur de code

print("Après l'exécution du tri à bulle :")
config_tri.display()



# Question 6 : Ecrire une machine RAM qui étant donné un automate `a pile ´ A et un mot w en entrée écrit 0 en sortie si w est reconnu par A et 1 sinon.
machine_produit = RAMProgram()
machine_produit.add_instruction(RAMInstruction("MULT", [1, 2, 3]))  # MULTIPLICATION (a * b)
machine_produit.add_instruction(RAMInstruction("JUMP", [1]))       # SAUTER À LA FIN DU PROGRAMME

config = RAMConfiguration(0, [0, 3, 5, 0, 0])  # Position du pointeur de code à 0, a = 3, b = 5, autres registres à zéro

print("Avant l'exécution de la machine RAM :")
config.display()
print("---------------")
while config.pos < len(machine_produit.instructions):
    config = execute_RAM_instruction(machine_produit, config)
    config.pos += 1  # Mise à jour de la position du pointeur de code
print("Après l'exécution de la machine RAM :")
config.display()



# Question 7 : Faire tourner cette machine RAM sur un automate à pile reconnaissant le langage {a puissanee n*b puissance n | n ∈ N}.
def simulate_APD(word, transitions):
    stack = [0]  # Initialiser la pile avec le symbole de fond de pile
    current_state = 0  # Initialiser l'état actuel

    # Parcours du mot
    for letter in word:
        # Recherche de la transition correspondante
        transition_found = False
        for transition in transitions:
            if transition[0] == current_state and transition[1] == int(letter) and transition[2] == stack[-1]:
                # Mettre à jour l'état et la pile selon la transition
                stack.pop()  # Retirer le symbole de la pile
                for symbol in reversed(transition[3]):  # Mettre les lettres du mot sur la pile
                    stack.append(int(symbol))
                current_state = transition[4]  # Mettre à jour l'état
                transition_found = True
                break

        # Si aucune transition correspondante n'est trouvée, le mot n'est pas reconnu
        if not transition_found:
            return 1  # Écriture de 1 en sortie

    # Vérifier si l'état final est atteint
    if current_state == 1:  # Si l'état final est atteint
        return 0  # Écriture de 0 en sortie
    else:
        return 1  # Écriture de 1 en sortie
    
# Exemple d'utilisation de la fonction simulate_APD avec un automate à pile donné
APD_transitions = [
    (0, 1, 0, "11", 1),  # Transition (état initial, lettre, symbole pile, mot, nouvel état)
    (1, 2, 0, "", 1)     # Transition (état final, lettre, symbole pile, mot, nouvel état final)
]

# Exécution de la simulation pour un mot spécifique
result = simulate_APD("11", APD_transitions)
print("Sortie de la machine RAM :", result)



# Question 8 : On va représenter le code de la RAM de mani`ere structurée par un graphe orienté. Chaque instruction est représentée par un sommet du graphe. Il y a un arc entre deux instructions si on peut passer de la premi`ere `a la seconde en un pas de calcul. Donner une fonction qui créé ce graphe `a partir du code d’une machine. Les instructions arithmétiques et le JUMP sont de degré sortant 1, tandis que les instructions conditionnelles sont de degré sortant 2.

class RAMGraph:
    def __init__(self):
        self.vertices = {}  # Dictionnaire pour stocker les sommets du graphe et leurs arcs sortants

    def add_vertex(self, instruction):
        self.vertices[instruction] = set()  # Initialisation des arcs sortants pour chaque sommet

    def add_edge(self, from_vertex, to_vertex):
        self.vertices[from_vertex].add(to_vertex)  # Ajout d'un arc sortant de from_vertex vers to_vertex

    def get_graph(self):
        return self.vertices  # Retourne le graphe complet


def build_RAM_graph(program):
    graph = RAMGraph()

    # Ajouter tous les sommets du graphe
    for instruction in program.instructions:
        graph.add_vertex(instruction)

    # Ajouter les arcs entre les instructions en fonction de leur type
    for i in range(len(program.instructions) - 1):  # Parcourir jusqu'à l'avant-dernière instruction
        instruction = program.get_instruction(i)
        next_instruction = program.get_instruction(i + 1)  # Récupérer l'instruction suivante

        if instruction.op in ["ADD", "SUB", "MULT", "DIV", "JUMP"]:
            # Arc sortant unique pour les instructions arithmétiques et JUMP
            graph.add_edge(instruction, next_instruction)
        elif instruction.op in ["JE", "JL"]:
            # Deux arcs sortants pour les instructions conditionnelles
            # Assurez-vous que la prochaine instruction existe avant d'ajouter l'arc
            if i + 2 < len(program.instructions):
                next_next_instruction = program.get_instruction(i + 2)  # Récupérer l'instruction après la prochaine
                graph.add_edge(instruction, next_instruction)
                graph.add_edge(instruction, next_next_instruction)

    return graph.get_graph()


# Affichage plus convivial des instructions
def print_instructions(instructions):
    instruction_strings = [str(instruction) for instruction in instructions]
    return "\n".join(instruction_strings)


# Exemple d'utilisation :
ram_graph = build_RAM_graph(program)
for vertex, edges in ram_graph.items():
    print(f"Instruction : {vertex}\nArcs sortants : {print_instructions(edges)}\n")



# Question 9 : On va appliquer une optimisation d’élimination du code mort. A partir du graphe représentant le code, calculer tous les sommets accessibles `a partir de la premi`ere instruction. Tous les sommets non accessibles correspondent `a des instructions qui ne seront jamais exécutées. Supprimer ces instructions dans votre code.
def find_accessible_vertices(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_vertex)
    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            find_accessible_vertices(graph, neighbor, visited)
    return visited


def remove_unreachable_instructions(program, accessible_vertices):
    instructions_to_remove = []
    for instruction in program.instructions:
        if instruction not in accessible_vertices:
            instructions_to_remove.append(instruction)

    for instruction in instructions_to_remove:
        program.instructions.remove(instruction)


# Calculer tous les sommets accessibles à partir de la première instruction
accessible_vertices = find_accessible_vertices(ram_graph, program.get_instruction(0))

# Supprimer les instructions non accessibles
remove_unreachable_instructions(program, accessible_vertices)

# Afficher le programme après l'élimination du code mort
print("Programme après l'élimination du code mort :")
for instruction in program.instructions:
    print(instruction)



