
class InstructionRAM:
    def __init__(self, opcode, operands):
        self.opcode = opcode  # Code opération de l'instruction
        self.operands = operands  # Opérandes de l'instruction

    def __str__(self):
        return f"{self.opcode} {' '.join(str(op) for op in self.operands)}"

class ProgrammeRAM:
    def __init__(self):
        self.instructions = []  # Liste des instructions

    def ajouter_instruction(self, opcode, operands):
        self.instructions.append(InstructionRAM(opcode, operands))  # Ajoute une instruction au programme

    def __str__(self):
        return '\n'.join(str(instruction) for instruction in self.instructions)




# Question 1

def lire_programme_ram(nom_fichier):
    programme_ram = ProgrammeRAM()
    with open(nom_fichier, 'r') as fichier:
        for ligne in fichier:
            tokens = ligne.strip().split()
            opcode = tokens[0]
            operands = [int(op) if op.isdigit() else op for op in tokens[1:]]
            programme_ram.ajouter_instruction(opcode, operands)
    return programme_ram

# Exemple d'utilisation :
nom_fichier = 'code_ram.txt'
programme_ram = lire_programme_ram(nom_fichier)
print(programme_ram)
print('\n')



# Question 2 
class ConfigurationRAM:
    def __init__(self, programme, registres):
        self.programme = programme  # Objet ProgrammeRAM
        self.registres = registres  # Dictionnaire (nom du registre -> valeur)

    def __str__(self):
        return f"Programme :\n{self.programme}\nRegistres : {self.registres}"
 
def executer_instruction(config, index_instruction):
    instruction = config.programme.instructions[index_instruction]
    opcode, operands = instruction.opcode, instruction.operands

    if opcode == 'ADD':
        config.registres[operands[2]] = config.registres[operands[0]] + config.registres[operands[1]]
    elif opcode == 'SUB':
        config.registres[operands[2]] = config.registres[operands[0]] - config.registres[operands[1]]
    elif opcode == 'MULT':
        config.registres[operands[2]] = config.registres[operands[0]] * config.registres[operands[1]]
    elif opcode == 'DIV':
        config.registres[operands[2]] = config.registres[operands[0]] // config.registres[operands[1]]
    elif opcode == 'JUMP':
        return index_instruction + operands[0]
    elif opcode == 'JE':
        if config.registres[operands[0]] == config.registres[operands[1]]:
            return index_instruction + operands[2]
    elif opcode == 'JL':
        if config.registres[operands[0]] < config.registres[operands[1]]:
            return index_instruction + operands[2]

    return index_instruction + 1


def executer_etape(config):
    prochaine_instruction_index = executer_instruction(config, 0)
    return ConfigurationRAM(config.programme, config.registres), prochaine_instruction_index

# Exemple d'utilisation :
programme = ProgrammeRAM()
programme.ajouter_instruction('ADD', ['i1', 'i2', 'r1'])
programme.ajouter_instruction('JUMP', [2])
registres_initiaux = {'i1': 5, 'i2': 3, 'r1': 0}
config_initiale = ConfigurationRAM(programme, registres_initiaux)

nouvelle_config, prochaine_instruction = executer_etape(config_initiale)
print(f"Nouveaux registres : {nouvelle_config.registres}")
print(f"Index de l'instruction suivante : {prochaine_instruction}")




# Question 3
def executer_jusqu_etat_final(mot, config):
    index_instruction = 0
    while index_instruction < len(config.programme.instructions):
        index_instruction = executer_instruction(config, index_instruction)

    return config.registres[mot]

# Exemple d'utilisation :
programme = ProgrammeRAM()
programme.ajouter_instruction('ADD', ['i1', 'i2', 'r1'])
programme.ajouter_instruction('JUMP', [2])
registres_initiaux = {'i1': 5, 'i2': 3, 'r1': 0}
config_initiale = ConfigurationRAM(programme, registres_initiaux)

mot_a_lire = 'r1'  # Choisissez le registre à lire comme sortie
resultat_final = executer_jusqu_etat_final(mot_a_lire, config_initiale)
print(f"Résultat final : {resultat_final}")




# Question 4
def afficher_configuration(config):
    print("Instructions du programme:")
    for i, instruction in enumerate(config.programme.instructions):
        print(f"{i}: {instruction.opcode} {instruction.operands}")
    print("\nRegistres:")
    for reg, value in config.registres.items():
        print(f"{reg}: {value}")
    print("\n")

def executer_etape(config):
    prochaine_instruction_index = executer_instruction(config, 0)
    afficher_configuration(config)
    return ConfigurationRAM(config.programme, config.registres), prochaine_instruction_index

# Exemple d'utilisation :
programme = ProgrammeRAM()
programme.ajouter_instruction('ADD', ['i1', 'i2', 'r1'])
programme.ajouter_instruction('JUMP', [2])
registres_initiaux = {'i1': 5, 'i2': 3, 'r1': 0}
config_initiale = ConfigurationRAM(programme, registres_initiaux)

nouvelle_config, prochaine_instruction = executer_etape(config_initiale)
print(f"Nouveaux registres : {nouvelle_config.registres}")
print(f"Index de l'instruction suivante : {prochaine_instruction}")




# Question 5