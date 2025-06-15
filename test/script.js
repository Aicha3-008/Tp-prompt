// Sélection des éléments
const display = document.getElementById('display');
const buttons = document.querySelectorAll('.btn');
const clearBtn = document.getElementById('clear');
const equalBtn = document.getElementById('equal');

// Ajout d’un écouteur pour chaque bouton
buttons.forEach(button => {
    const value = button.dataset.value;
    if (value) {
        button.addEventListener('click', () => {
            display.value += value;
        });
    }
});

// Effacer l'affichage
clearBtn.addEventListener('click', () => {
    display.value = '';
});

// Évaluer l'expression
equalBtn.addEventListener('click', () => {
    try {
        display.value = eval(display.value);
    } catch (e) {
        display.value = 'Erreur';
    }
});
