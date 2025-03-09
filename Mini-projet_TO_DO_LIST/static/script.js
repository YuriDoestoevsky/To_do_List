function setTheme(theme) {
    const body = document.body;
    body.classList.remove('dark-theme', 'ark-theme');
    if (theme === 'dark') {
        body.classList.add('dark-theme');
    }
    // Save the selected theme to localStorage
    localStorage.setItem('theme', theme);
}

function applySavedTheme() {
    const savedTheme = localStorage.getItem('theme') || 'normal';
    setTheme(savedTheme);
}

window.onload = applySavedTheme;