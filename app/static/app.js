const API_URL = '/applications/';

const STATUS_ORDER = {
    'offer': 1,
    'interview': 2,
    'applied': 3,
    'rejected': 4
};

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    fetchApplications();
});

function initTheme() {
    const themeToggle = document.getElementById('theme-toggle');
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        themeToggle.innerText = '☀️ Light Mode';
    }

    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        const isDark = document.body.classList.contains('dark-mode');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
        themeToggle.innerText = isDark ? 'Light Mode' : 'Dark Mode';
    });
}

async function fetchApplications() {
    try {
        const response = await fetch(API_URL);
        let applications = await response.json();

        applications.sort((a, b) => {
            const orderA = STATUS_ORDER[a.status] || 99;
            const orderB = STATUS_ORDER[b.status] || 99;
            return orderA - orderB;
        });

        renderTable(applications);
    } catch (error) {
        console.error('Fehler beim Laden der Bewerbungen:', error);
    }
}

function renderTable(applications) {
    const tbody = document.getElementById('job-list');
    tbody.innerHTML = '';

    if (applications.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" style="text-align:center; color: var(--text-muted); padding: 20px;">Noch keine Bewerbungen vorhanden.</td></tr>';
        return;
    }

    applications.forEach(app => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>#${app.id}</td>
            <td><strong>${escapeHtml(app.company)}</strong></td>
            <td>${escapeHtml(app.role)}</td>
            <td>
                <select class="status-select status-${app.status}" onchange="updateStatus(${app.id}, this.value)">
                    <option value="applied" ${app.status === 'applied' ? 'selected' : ''}>Beworben</option>
                    <option value="interview" ${app.status === 'interview' ? 'selected' : ''}>Interview</option>
                    <option value="offer" ${app.status === 'offer' ? 'selected' : ''}>Zusage</option>
                    <option value="rejected" ${app.status === 'rejected' ? 'selected' : ''}>Absage</option>
                </select>
            </td>
            <td>
                <button class="btn btn-danger" onclick="deleteApplication(${app.id})">Löschen</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

document.getElementById('add-job-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const company = document.getElementById('company').value;
    const role = document.getElementById('role').value;
    const status = document.getElementById('status').value;

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ company, role, status })
        });

        if (response.ok) {
            document.getElementById('add-job-form').reset();
            fetchApplications();
        } else {
            alert('Fehler beim Erstellen der Bewerbung.');
        }
    } catch (error) {
        console.error('Fehler:', error);
    }
});

async function updateStatus(id, newStatus) {
    try {
        const response = await fetch(`${API_URL}${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status: newStatus })
        });

        if (response.ok) {
            fetchApplications();
        } else {
            alert('Fehler beim Aktualisieren des Status.');
            fetchApplications();
        }
    } catch (error) {
        console.error('Fehler:', error);
    }
}

async function deleteApplication(id) {
    if (!confirm(`Möchtest du die Bewerbung #${id} wirklich löschen?`)) return;

    try {
        const response = await fetch(`${API_URL}${id}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            fetchApplications();
        } else {
            alert('Fehler beim Löschen.');
        }
    } catch (error) {
        console.error('Fehler:', error);
    }
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.innerText = text;
    return div.innerHTML;
}