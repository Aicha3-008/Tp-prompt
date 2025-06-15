# TP - Ingénierie de Prompt appliquée à la génération de code avec l’IA 🤖

##  Encadré par :
Prof. Imane Allaouzi
## 🎯 Objectif du TP

Ce TP a pour but d'apprendre à concevoir des **prompts efficaces** pour générer du **code de qualité avec une IA générative**, en suivant les principes fondamentaux :
- **Tâche**
- **Contexte**
- **Références**
- **Évaluation**
- **Itération**

---

## 🧠 Partie 1 – Choix de la solution d'IA générative
# TP - Ingénierie de Prompt appliquée à la génération de code avec l’IA 🤖💻

## 👩‍🏫 Encadré par :
Prof. Imane Allaouzi

---

## 🎯 Objectif du TP

Ce TP a pour but d'apprendre à concevoir des **prompts efficaces** pour générer du **code de qualité avec une IA générative**, en suivant les principes fondamentaux :
- **Tâche**
- **Contexte**
- **Références**
- **Évaluation**
- **Itération**

---

## 🧠 Partie 1 – Choix de la solution d'IA générative

### ✅ Solution choisie : **ChatGPT (OpenAI)**

### 🔍 Définition brève :
ChatGPT est un assistant conversationnel développé par OpenAI, capable de générer, corriger, améliorer et expliquer du code à partir de requêtes en langage naturel.

### ✔️ Avantages :
- Génération rapide de code multi-langage (Python, JS, HTML, etc.).
- Peut expliquer les erreurs, refactorer et optimiser du code existant.
- Répond de manière interactive et personnalisée avec contexte.

### ⚠️ Inconvénients :
- Peut produire du code incorrect sans prévenir.
- Ne comprend pas toujours les besoins implicites.
- Pas d’accès direct à l’environnement de test ou de compilation.

### 💼 Cas d’utilisation typiques :
- Génération de fonctions ou algorithmes simples ou complexes.
- Rédaction de docstrings et fichiers `README.md`.
- Débogage et amélioration de code existant.
- Simulation de comportements utilisateur (persona).

## 🧠 Partie 2 – Génération de code avec IA
# Exercice 2.1 : Génération de code Python pour une tâche de calcul :
•Prompt Vague :
->La fonction `calculate(a, b, op)` est clairement nommée de manière pertinente et descriptive. Elle prend en charge les quatre opérations mathématiques de base : addition, soustraction, multiplication et division, avec un arrondi à deux décimales pour cette dernière. Elle intègre une gestion d’erreurs efficace en levant une `ZeroDivisionError` en cas de division par zéro et une `ValueError` pour tout opérateur invalide, ce qui la rend robuste. Enfin, elle est accompagnée d’un docstring complet qui décrit les paramètres, le retour, les exceptions et l’objectif de la fonction, assurant ainsi une documentation claire et professionnelle.


•Prompt Spécifique :
-> Les deux fonctions `calculate(a, b, op)` sont bien nommées, robustes et respectent les conventions PEP8, mais la seconde version se distingue par une **meilleure structure défensive**. Contrairement à la première, qui vérifie les erreurs au fur et à mesure dans chaque bloc `elif`, la seconde commence par une **vérification centralisée de la validité de l'opérateur**, ce qui permet d'arrêter l'exécution immédiatement en cas d’entrée invalide. Côté **lisibilité**, les deux versions sont bien documentées avec un docstring clair et complet, mais la deuxième est légèrement plus lisible grâce à des commentaires séparés pour chaque bloc d'opération. En ce qui concerne la **couverture des cas**, les deux versions prennent en charge les quatre opérations mathématiques de base avec gestion de la division par zéro, mais la seconde **améliore la clarté logique** en plaçant la validation des erreurs avant l’exécution de toute opération. En résumé, bien que les deux soient solides, la deuxième version est **plus structurée, défensive et proprement segmentée**, ce qui la rend plus facile à maintenir.


•Prompt avec Persona :
->Oui, ce code est plus professionnel car il respecte les conventions PEP8, inclut un docstring clair et détaillé, et utilise des exceptions explicites pour gérer les erreurs comme les opérateurs invalides ou la division par zéro. Il est également mieux structuré grâce à une validation initiale de l’opérateur, un enchaînement logique des conditions, et une organisation claire qui facilite la lecture et la maintenance. Enfin, il est plus sécurisé car il anticipe les erreurs critiques et limite l’exécution aux seuls cas prévus, garantissant ainsi un comportement fiable et contrôlé.

# Analyse Critique:
1) Différences entre les codes générés :

Chaque prompt a produit une version différente de la fonction calculate. Le 
premier, très vague, a donné un code basique, sans vérification des erreurs, 
sans commentaires ni explication. Le second prompt, un peu plus précis, a 
généré une fonction correcte avec la gestion de la division par zéro, des 
opérateurs invalides et un arrondi pour la division, mais toujours sans 
vérification des types ou structure avancée. Enfin, le prompt le plus 
détaillé, avec des consignes claires sur la qualité attendue (PEP8, erreurs, 
docstring), a permis de générer une fonction complète, professionnelle, bien 
commentée, et respectant les bonnes pratiques de Python. On voit donc 
clairement que plus le prompt est précis, plus la qualité du code est élevée.

2) Principe de prompt engineering le plus impactant :

Parmi les principes de prompt engineering (clarté, spécificité, persona), 
c’est la spécificité qui a eu le plus d’impact. En donnant des détails très 
précis sur ce que la fonction devait faire (types des données, erreurs à 
gérer, style PEP8, docstring, etc.), l’IA a pu produire un code bien 
structuré, robuste et directement réutilisable. Sans ces précisions, l’IA 
reste dans une réponse générique. La clarté et l’utilisation d’un persona 
(ex. "en tant que développeur Python") aident aussi, mais c’est la 
spécificité qui change vraiment la qualité du résultat.

3) Erreurs ou comportements inattendus :

Oui, l’IA a introduit des lacunes dans la première version. Par exemple, 
elle ne vérifie pas si les entrées sont bien des entiers, et ne gère pas 
proprement les erreurs comme une division par zéro ou un opérateur invalide. 
Ces oublis peuvent provoquer des bugs ou des plantages si on utilise la 
fonction dans un vrai programme. À partir du deuxième prompt, ces erreurs 
sont corrigées car les consignes sont plus claires.

4) Coût en temps et en effort : prompt vague vs. prompt spécifique :

Un prompt vague demande peu d’effort au départ, mais entraîne souvent 
beaucoup de travail ensuite pour corriger et améliorer le code (ajouter des 
vérifications, commentaires, etc.). À l’inverse, un prompt spécifique 
demande un peu plus de temps à formuler, mais il permet d’obtenir un code de 
qualité dès le départ, ce qui fait gagner du temps au final. Donc, mieux 
vaut prendre quelques secondes de plus pour bien formuler sa demande, plutôt 
que corriger un code incomplet ensuite.

# Exercice 2.2 : Génération d'une fonction en  Python  :
• zéro-Shot Prompting:
->Oui, le code est correct et robuste. Il vérifie que l’entrée est bien une 
chaîne de 10 caractères alphanumériques, et lève des erreurs claires si ce 
n’est pas le cas. Le format appliqué (`XXX-XXXX-XXX`) est respecté, et le 
code est bien structuré avec un docstring clair et conforme aux bonnes 
pratiques.
• One-Shot Prompting :
->Oui, l’ajout d’un exemple concret dans le prompt a clairement simplifié la 
tâche de l’IA et renforcé la précision du résultat. Contrairement à la 
version précédente où le format était basé uniquement sur une description 
textuelle (`XXX-XXXX-XXX`), cette version utilise un exemple d’entrée-sortie 
explicite (`"ABC123DEF4"` → `"ABC-123-DEF4"`), ce qui a permis à l’IA 
d’appliquer le bon découpage (après le 3e et le 6e caractère). Cela évite 
toute ambiguïté et corrige l’erreur précédente où le format appliqué ne 
correspondait pas exactement à l’intention. En résumé, l’exemple fourni a 
permis une meilleure compréhension et a réduit le risque d’erreur de format.
• Few-Shot prompting :
-> Oui, l’IA gère nettement mieux les cas d’erreur dans cette version. Grâce 
aux exemples positifs et négatifs intégrés (cas valide et cas invalide comme 
`"SHORT"`), la fonction est plus robuste : elle vérifie explicitement que 
l'entrée est une chaîne, qu'elle contient exactement 10 caractères, et 
qu'elle est alphanumérique. Les messages d'erreur sont clairs et précis, ce 
qui facilite le débogage et l’utilisation sécurisée de la fonction. L’ajout 
de plusieurs exemples dans le prompt (Few-Shot Prompting) a donc renforcé la 
compréhension du format attendu et permis de traiter les erreurs de manière 
complète et fiable.

## Analyse Critique :
1)  Influence des exemples sur la compréhension de l’IA
L’ajout d’exemples, en particulier d’entrées-sorties précises (comme 
"ABC123DEF4" → "ABC-123-DEF4"), améliore considérablement la compréhension 
de l’IA, surtout lorsqu’il s’agit de règles complexes ou de formats 
spécifiques. Les exemples agissent comme des cas concrets qui réduisent 
l’ambiguïté du langage naturel. Cela permet à l’IA de mieux interpréter la 
logique attendue (comme où insérer les tirets) et de générer un code 
conforme à l’intention réelle. En ajoutant également des cas d’erreur, l’IA 
est plus encline à intégrer des vérifications robustes (longueur, type, 
alphanumérique) et à lever des exceptions appropriées. Ainsi, les exemples
servent à guider le raisonnement de l’IA et renforcent la fiabilité du code 
généré.

2) Utilité du Few-Shot Prompting en développement
Le Few-Shot Prompting est particulièrement utile lorsque :

• La tâche est complexe ou spécifique, avec des règles métiers ou de format 
non standard.

• On veut éviter les erreurs logiques dans le code généré.

• On cherche à générer du code robuste, notamment avec une bonne gestion des 
cas limites et des erreurs.

• On veut reproduire un comportement conforme à des exemples concrets, plutôt qu’à une description abstraite.

• Il est aussi très efficace pour enseigner à l’IA le style attendu, que ce 
soit dans le formatage du code, les noms de fonctions, ou la rédaction de 
docstring.

3) Limites des exemples (nombre, qualité)
-> Oui, il existe des limites :
• Trop d’exemples peuvent rendre le prompt lourd, ralentir la réponse de 
l’IA ou même la perturber si les exemples sont contradictoires ou mal 
choisis.

• La qualité est essentielle : un exemple mal conçu (erreur de format, nom 
trompeur) peut induire l’IA en erreur.

• Si les exemples ne couvrent pas les cas d'erreur ou les exceptions, l’IA 
risque de ne pas anticiper ces situations.

• Enfin, les exemples doivent rester représentatifs de ce qu’on attend 
réellement ; s’ils sont trop simples, l’IA risque de généraliser 
incorrectement.

# Exercice 2.3 : Génération d'un petit site web en  Python  :
1) "Crée une mini-application Web qui simule une calculatrice avec HTML, CSS 
et JavaScript." 
=>Le résultat du prompt vague donne une calculatrice très basique, avec une interface peu soignée, des boutons mal alignés, aucun style responsive, et une logique JavaScript minimale souvent écrite en bloc. Il n’y a pas de gestion d’erreurs, ni de séparation claire entre HTML, CSS et JS, ce qui rend le code difficile à maintenir et peu adapté à une utilisation sérieuse.

2) "Tu es un développeur web expérimenté, avec... cites au 
niveau de la consigne "

3) L’évaluation des différentes versions de prompts montre clairement 
l’impact de la formulation sur la qualité du code généré. Un prompt vague, 
comme “Crée une mini-calculatrice en HTML, CSS et JS”, donne un résultat 
très basique : une interface minimaliste, peu ou pas de style, et un code 
JavaScript peu structuré, sans gestion des erreurs. Lorsque le prompt inclut 
quelques détails techniques (types de boutons, affichage, style moderne, 
gestion des erreurs), la calculatrice devient plus fonctionnelle, mieux 
présentée, avec un début de structure et une certaine logique de validation. 
En revanche, le prompt structuré avec une persona (développeur expérimenté) 
et des contraintes précises (responsivité, accessibilité, HTML/CSS/JS pur, 
pas de framework) aboutit à un code complet, bien organisé et maintenable. 
L’interface est esthétique, le JavaScript est clair et modulaire, et 
l’application est utilisable aussi bien sur ordinateur que sur mobile. En 
résumé, plus le prompt est détaillé et contextualisé, plus l’IA génère un 
code robuste, lisible et proche d’un résultat professionnel.

## 🧠 Partie 3 – Débogage et Amélioration du Code
# Exercice 3.2 :
1) Le code initial trie une liste d'entiers en ordre croissant à l'aide d’un 
algorithme simple de type sélection ou bulle, mais il présente plusieurs 
défauts de lisibilité. Il est écrit en bloc sans fonction, avec des noms de 
variables peu explicites (a, i, j, tmp), aucun commentaire ni docstring, ne 
respecte pas la convention PEP8, et n'inclut pas de bloc conditionnel if 
__name__ == "__main__", ce qui rend sa lecture, sa maintenance et sa 
réutilisation difficiles.

# Exercice 3.3 : Génération de Documentation
3) évaluation :
• Clarté : La docstring et le README sont très lisibles.
• Complétude : Tous les éléments demandés sont présents : but, paramètres, retour, exemple.
• Facilité de compréhension : Oui, même un nouveau développeur peut comprendre l’usage de la fonction rapidement.



