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

---
## 🧠 Partie 2 – Génération de code avec IA
# Exercice 2.1 : Génération de code Python pour une tâche de calcul :
•Prompt Vague :
->La fonction `calculate(a, b, op)` est clairement nommée de manière pertinente et descriptive. Elle prend en charge les quatre opérations mathématiques de base : addition, soustraction, multiplication et division, avec un arrondi à deux décimales pour cette dernière. Elle intègre une gestion d’erreurs efficace en levant une `ZeroDivisionError` en cas de division par zéro et une `ValueError` pour tout opérateur invalide, ce qui la rend robuste. Enfin, elle est accompagnée d’un docstring complet qui décrit les paramètres, le retour, les exceptions et l’objectif de la fonction, assurant ainsi une documentation claire et professionnelle.


•Prompt Spécifique :
-> Les deux fonctions `calculate(a, b, op)` sont bien nommées, robustes et respectent les conventions PEP8, mais la seconde version se distingue par une **meilleure structure défensive**. Contrairement à la première, qui vérifie les erreurs au fur et à mesure dans chaque bloc `elif`, la seconde commence par une **vérification centralisée de la validité de l'opérateur**, ce qui permet d'arrêter l'exécution immédiatement en cas d’entrée invalide. Côté **lisibilité**, les deux versions sont bien documentées avec un docstring clair et complet, mais la deuxième est légèrement plus lisible grâce à des commentaires séparés pour chaque bloc d'opération. En ce qui concerne la **couverture des cas**, les deux versions prennent en charge les quatre opérations mathématiques de base avec gestion de la division par zéro, mais la seconde **améliore la clarté logique** en plaçant la validation des erreurs avant l’exécution de toute opération. En résumé, bien que les deux soient solides, la deuxième version est **plus structurée, défensive et proprement segmentée**, ce qui la rend plus facile à maintenir.


•Prompt avec Persona :
->Oui, ce code est plus professionnel car il respecte les conventions PEP8, inclut un docstring clair et détaillé, et utilise des exceptions explicites pour gérer les erreurs comme les opérateurs invalides ou la division par zéro. Il est également mieux structuré grâce à une validation initiale de l’opérateur, un enchaînement logique des conditions, et une organisation claire qui facilite la lecture et la maintenance. Enfin, il est plus sécurisé car il anticipe les erreurs critiques et limite l’exécution aux seuls cas prévus, garantissant ainsi un comportement fiable et contrôlé.


