# RAM Simulator

Ce programme Python simule l'exécution d'une machine RAM (Random Access Machine) en utilisant un programme donné et une configuration initiale. Il lit un programme RAM à partir d'un fichier texte, exécute les instructions étape par étape et affiche les configurations intermédiaires.

## Utilisation

1. **Créer un fichier de programme RAM :**

   - Créez un fichier texte (par exemple, `code_ram.txt`) contenant les instructions RAM. Chaque instruction doit être sur une ligne séparée.
   - Exemple :
     ```
     ADD i1 i2 r1
     JUMP 2
     ```

2. **Exécuter le simulateur :**

   - Exécutez le script Python (`ram_simulator.py`) avec le fichier de programme en argument.
   - Exemple :
     ```
     python ram_simulator.py code_ram.txt
     ```

3. **Afficher les configurations intermédiaires :**
   - Le simulateur affichera les instructions du programme et les valeurs actuelles des registres à chaque étape.
   - La simulation se poursuit jusqu'à ce que le programme atteigne la fin.

## Instructions RAM

- `ADD(r1, r2, r3)`: Ajoute les valeurs dans les registres `r1` et `r2`, stocke le résultat dans `r3`.
- `SUB(r1, r2, r3)`: Soustrait la valeur dans le registre `r2` de `r1`, stocke le résultat dans `r3`.
- `MULT(r1, r2, r3)`: Multiplie les valeurs dans les registres `r1` et `r2`, stocke le résultat dans `r3`.
- `DIV(r1, r2, r3)`: Divise la valeur dans le registre `r1` par `r2`, stocke le quotient entier dans `r3`.
- `JUMP(z)`: Sauter `z` instructions en avant.
- `JE(r1, r2, z)`: Si la valeur dans `r1` est égale à la valeur dans `r2`, sauter `z` instructions en avant.
- `JL(r1, r2, z)`: Si la valeur dans `r1` est inférieure à la valeur dans `r2`, sauter `z` instructions en avant.

## Exemple

Supposons que nous ayons le programme suivant :

```
ADD i1 i2 r1
JUMP 2
```

Et les registres initiaux : `i1=5`, `i2=3`, `r1=0`.

Le simulateur exécutera le programme étape par étape et affichera les configurations intermédiaires.

---

N'hésitez pas à personnaliser ce README en fonction de votre implémentation spécifique et de toute fonctionnalité supplémentaire que vous avez ajoutée. Si vous avez d'autres questions ou avez besoin d'aide supplémentaire, n'hésitez pas à me le faire savoir ! 😊
