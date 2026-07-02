function changeTheme(theme) {
    const root = document.documentElement; 
    root.classList.remove('theme-light', 'theme-dark', 'theme-dracula-light', 'theme-dracula-dark');
    root.classList.add(`theme-${theme}`);
    localStorage.setItem('selected-theme', theme);
}

function toggleMenu() {
    const nav = document.getElementById('site-nav');
    nav.classList.toggle('active');
}

window.onload = () => {
    const savedTheme = localStorage.getItem('selected-theme') || `dracula-${getSystemTheme()}`;
    document.getElementById('theme-selector').value = savedTheme;
    changeTheme(savedTheme);
};

const getSystemTheme = () => {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
};

document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll("a");
    links.forEach(link => {
        if (link.hostname !== window.location.hostname) {
        link.setAttribute("target", "_blank");
        link.setAttribute("rel", "noopener noreferrer");
        }
    });
});