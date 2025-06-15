# 🤖💻 TP - Ingénierie de Prompt appliquée à la génération de code avec l'IA

<div align="center">

![AI Code Generation](https://img.shields.io/badge/AI-Code%20Generation-blue?style=for-the-badge&logo=openai)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&lines=Prompt+Engineering+for+AI+Code+Generation;Learning+Effective+AI+Prompting+Techniques;Building+Quality+Code+with+AI+Assistance" alt="Typing SVG" />

</div>

---

## 👩‍🏫 **Encadré par :**
<div align="center">
<h3>Prof. Imane Allaouzi</h3>
</div>

---

## 🎯 **Objectif du TP**

<div align="center">

> Ce TP a pour but d'apprendre à concevoir des **prompts efficaces** pour générer du **code de qualité avec une IA générative**

</div>

### 🔥 Principes fondamentaux :

<table>
<tr>
<td align="center">🎯</td>
<td><strong>Tâche</strong></td>
<td>Définir clairement l'objectif</td>
</tr>
<tr>
<td align="center">🌐</td>
<td><strong>Contexte</strong></td>
<td>Fournir le cadre d'utilisation</td>
</tr>
<tr>
<td align="center">📚</td>
<td><strong>Références</strong></td>
<td>Utiliser des exemples concrets</td>
</tr>
<tr>
<td align="center">⚡</td>
<td><strong>Évaluation</strong></td>
<td>Mesurer la qualité du résultat</td>
</tr>
<tr>
<td align="center">🔄</td>
<td><strong>Itération</strong></td>
<td>Améliorer par étapes</td>
</tr>
</table>

---

## 🧠 **Partie 1 – Choix de la solution d'IA générative**

<div align="center">

### ✅ **Solution choisie : ChatGPT (OpenAI)**

<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" />

</div>

### 🔍 **Définition brève :**
ChatGPT est un assistant conversationnel développé par OpenAI, capable de générer, corriger, améliorer et expliquer du code à partir de requêtes en langage naturel.

<details>
<summary><strong>✔️ Avantages</strong></summary>

- 🚀 Génération rapide de code multi-langage (Python, JS, HTML, etc.)
- 🔧 Peut expliquer les erreurs, refactorer et optimiser du code existant
- 💬 Répond de manière interactive et personnalisée avec contexte

</details>

<details>
<summary><strong>⚠️ Inconvénients</strong></summary>

- ❌ Peut produire du code incorrect sans prévenir
- 🤔 Ne comprend pas toujours les besoins implicites
- 🔌 Pas d'accès direct à l'environnement de test ou de compilation

</details>

### 💼 **Cas d'utilisation typiques :**

```mermaid
graph TD
    A[💡 Génération de code] --> B[📝 Fonctions & Algorithmes]
    A --> C[📖 Documentation]
    A --> D[🐛 Débogage]
    A --> E[👤 Simulation Persona]
    
    B --> B1[Simple]
    B --> B2[Complexe]
    
    C --> C1[Docstrings]
    C --> C2[README.md]
    
    D --> D1[Correction bugs]
    D --> D2[Optimisation]
```

---

## 🧠 **Partie 2 – Génération de code avec IA**

### 📊 **Exercice 2.1 : Génération de code Python pour une tâche de calcul**

<div align="center">

| Type de Prompt | Qualité du Code | Robustesse | Documentation |
|----------------|-----------------|------------|---------------|
| 🟡 **Prompt Vague** | ⭐⭐ | ⭐ | ⭐ |
| 🟠 **Prompt Spécifique** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 🟢 **Prompt avec Persona** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

</div>

#### 🔍 **Analyse Critique :**

<details>
<summary><strong>1️⃣ Différences entre les codes générés</strong></summary>

Chaque prompt a produit une version différente de la fonction `calculate`. Le premier, très vague, a donné un code basique, sans vérification des erreurs, sans commentaires ni explication. Le second prompt, un peu plus précis, a généré une fonction correcte avec la gestion de la division par zéro, des opérateurs invalides et un arrondi pour la division, mais toujours sans vérification des types ou structure avancée. Enfin, le prompt le plus détaillé, avec des consignes claires sur la qualité attendue (PEP8, erreurs, docstring), a permis de générer une fonction complète, professionnelle, bien commentée, et respectant les bonnes pratiques de Python.

> **📈 Conclusion :** Plus le prompt est précis, plus la qualité du code est élevée.

</details>

<details>
<summary><strong>2️⃣ Principe de prompt engineering le plus impactant</strong></summary>

Parmi les principes de prompt engineering (clarté, spécificité, persona), c'est la **spécificité** qui a eu le plus d'impact. En donnant des détails très précis sur ce que la fonction devait faire (types des données, erreurs à gérer, style PEP8, docstring, etc.), l'IA a pu produire un code bien structuré, robuste et directement réutilisable.

> **🎯 Point clé :** La spécificité change vraiment la qualité du résultat.

</details>

<details>
<summary><strong>3️⃣ Erreurs ou comportements inattendus</strong></summary>

Oui, l'IA a introduit des lacunes dans la première version. Par exemple, elle ne vérifie pas si les entrées sont bien des entiers, et ne gère pas proprement les erreurs comme une division par zéro ou un opérateur invalide. Ces oublis peuvent provoquer des bugs ou des plantages si on utilise la fonction dans un vrai programme.

> **⚠️ Important :** À partir du deuxième prompt, ces erreurs sont corrigées car les consignes sont plus claires.

</details>

<details>
<summary><strong>4️⃣ Coût en temps et en effort</strong></summary>

Un prompt vague demande peu d'effort au départ, mais entraîne souvent beaucoup de travail ensuite pour corriger et améliorer le code. À l'inverse, un prompt spécifique demande un peu plus de temps à formuler, mais il permet d'obtenir un code de qualité dès le départ.

> **⏰ Conseil :** Mieux vaut prendre quelques secondes de plus pour bien formuler sa demande.

</details>

---

### 🎯 **Exercice 2.2 : Génération d'une fonction Python**

<div align="center">

```mermaid
graph LR
    A[🎯 Zero-Shot] --> B[📝 One-Shot] --> C[📚 Few-Shot]
    
    A --> A1[Code basique]
    B --> B1[Meilleure précision]
    C --> C1[Code robuste]
    
    style A fill:#ffcccc
    style B fill:#ffffcc
    style C fill:#ccffcc
```

</div>

#### 📈 **Progression de la qualité :**

| Technique | Robustesse | Gestion d'erreurs | Clarté |
|-----------|------------|-------------------|---------|
| **Zero-Shot** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **One-Shot** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Few-Shot** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

#### 🔍 **Analyse Critique :**

<details>
<summary><strong>1️⃣ Influence des exemples sur la compréhension de l'IA</strong></summary>

L'ajout d'exemples, en particulier d'entrées-sorties précises (comme "ABC123DEF4" → "ABC-123-DEF4"), améliore considérablement la compréhension de l'IA, surtout lorsqu'il s'agit de règles complexes ou de formats spécifiques. Les exemples agissent comme des cas concrets qui réduisent l'ambiguïté du langage naturel.

> **🎯 Impact :** Les exemples servent à guider le raisonnement de l'IA et renforcent la fiabilité du code généré.

</details>

<details>
<summary><strong>2️⃣ Utilité du Few-Shot Prompting en développement</strong></summary>

Le Few-Shot Prompting est particulièrement utile lorsque :

- 🔧 **Tâche complexe** : règles métiers ou de format non standard
- ❌ **Éviter les erreurs logiques** dans le code généré
- 🛡️ **Code robuste** : bonne gestion des cas limites et erreurs
- 📋 **Comportement conforme** : exemples concrets vs description abstraite
- 🎨 **Style cohérent** : formatage, noms de fonctions, docstring

</details>

<details>
<summary><strong>3️⃣ Limites des exemples (nombre, qualité)</strong></summary>

⚠️ **Limites identifiées :**

- 📚 **Trop d'exemples** : prompt lourd, réponse lente, confusion possible
- 🎯 **Qualité essentielle** : un exemple mal conçu induit l'IA en erreur
- 🚫 **Couverture incomplète** : manquer les cas d'erreur ou exceptions
- 📊 **Représentativité** : exemples trop simples = généralisation incorrecte

</details>

---

### 🌐 **Exercice 2.3 : Génération d'un site web**

<div align="center">

#### 🎨 **Évolution de la qualité selon le prompt**

```mermaid
graph TD
    A[🟡 Prompt Vague] --> A1[Interface basique]
    A --> A2[Style minimal]
    A --> A3[Code non structuré]
    
    B[🟠 Prompt Détaillé] --> B1[Interface fonctionnelle]
    B --> B2[Style moderne]
    B --> B3[Début de structure]
    
    C[🟢 Prompt + Persona] --> C1[Interface professionnelle]
    C --> C2[Design responsive]
    C --> C3[Code maintenable]
    
    style A fill:#ffcccc
    style B fill:#ffffcc
    style C fill:#ccffcc
```

</div>

#### 📊 **Comparaison des résultats :**

| Aspect | Prompt Vague | Prompt Détaillé | Prompt + Persona |
|--------|-------------|-----------------|------------------|
| **Interface** | Minimaliste | Fonctionnelle | Professionnelle |
| **Responsive** | ❌ | ⚠️ | ✅ |
| **Accessibilité** | ❌ | ⚠️ | ✅ |
| **Structure code** | Monolithique | Organisée | Modulaire |
| **Gestion erreurs** | ❌ | ⚠️ | ✅ |

> **🏆 Conclusion :** Plus le prompt est détaillé et contextualisé, plus l'IA génère un code robuste, lisible et proche d'un résultat professionnel.

---

## 🧠 **Partie 3 – Débogage et Amélioration du Code**

### 🔧 **Exercice 3.2 : Amélioration de code**

<div align="center">

#### **🔄 Transformation du Code**

```mermaid
graph LR
    A[😵 Code Initial] --> B[🔧 Analyse IA] --> C[✨ Code Amélioré]
    
    A --> A1[Variables cryptiques]
    A --> A2[Pas de structure]
    A --> A3[Aucune documentation]
    
    C --> C1[Noms explicites]
    C --> C2[Fonctions claires]
    C --> C3[Documentation complète]
    
    style A fill:#ffcccc
    style C fill:#ccffcc
```

</div>

#### 📝 **Problèmes identifiés dans le code initial :**

- 🔤 **Variables peu explicites** : `a`, `i`, `j`, `tmp`
- 📚 **Pas de fonction** : code écrit en bloc
- 📝 **Aucun commentaire** ni docstring
- 🎨 **PEP8 non respecté**
- 🏗️ **Pas de structure** `if __name__ == "__main__"`

---

### 📖 **Exercice 3.3 : Génération de Documentation**

<div align="center">

#### **📊 Évaluation de la documentation générée**

| Critère | Note | Commentaire |
|---------|------|-------------|
| **Clarté** | ⭐⭐⭐⭐⭐ | Docstring et README très lisibles |
| **Complétude** | ⭐⭐⭐⭐⭐ | Tous les éléments présents |
| **Compréhension** | ⭐⭐⭐⭐⭐ | Accessible aux nouveaux développeurs |

</div>

#### ✅ **Éléments documentés :**

- 🎯 **But de la fonction**
- 📥 **Paramètres d'entrée**
- 📤 **Valeur de retour**
- 💡 **Exemple d'utilisation**
- ⚠️ **Gestion des erreurs**

---

## 🚀 **Conclusion & Apprentissages**

<div align="center">

### 🎯 **Points Clés Retenus**

</div>

```mermaid
mindmap
  root((Prompt Engineering))
    Spécificité
      Détails techniques
      Contraintes claires
      Format attendu
    Exemples
      Zero-Shot
      One-Shot
      Few-Shot
    Persona
      Contexte professionnel
      Niveau d'expertise
      Style de code
    Itération
      Amélioration continue
      Feedback
      Raffinement
```

### 🏆 **Bonnes Pratiques Identifiées**

1. **📝 Commencer spécifique** plutôt que d'itérer depuis le vague
2. **💡 Utiliser des exemples concrets** pour les tâches complexes  
3. **👤 Définir une persona** pour un contexte professionnel
4. **🔄 Itérer et améliorer** le prompt selon les résultats
5. **⚠️ Toujours demander la gestion d'erreurs** explicitement

---

<div align="center">

### 🎓 **Merci pour votre attention !**

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=16&pause=1000&color=36BCF7&center=true&vCenter=true&width=400&lines=Happy+Prompting!;Code+with+AI+Efficiently!;Keep+Learning!" alt="Typing SVG" />

---

**Made with ❤️ for Prompt Engineering Learning**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com)

</div>
