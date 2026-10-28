const API_URL = '/applications/';

document.addEventListener('DOMContentLoaded', fetchApplications);

async function fetchApplications() {
    try {
        const response = await fetch(API_URL);
        const applications = await response.json();
        renderTable(applications);
    } catch (error) {
        console.error('Fehler beim Laden der Bewerbungen:', error);
    }
}

function renderTable(applications) {
    const tbody = document.getElementById('job-list');
    tbody.innerHTML = '';

    if (applications.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" style="text-align:center; color: #718096; padding: 20px;">Noch keine Bewerbungen vorhanden.</td></tr>';
        return;
    }

    applications.forEach(app => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>#${app.id}</td>
            <td><strong>${escapeHtml(app.company)}</strong></td>
            <td>${escapeHtml(app.role)}</td>
            <td>
                <select class="status-select" onchange="updateStatus(${app.id}, this.value)">
                    <option value="applied" ${app.status === 'applied' ? 'selected' : ''}>Beworben</option>
                    <option value="interview" ${app.status === 'interview' ? 'selected' : ''}>Interview</option>
                    <option value="offer" ${app.status === 'offer' ? 'selected' : ''}>Zusage</option>
                    <option value="rejected" ${app.status === 'rejected' ? 'selected' : ''}>rAbsage</option>
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

        if (!response.ok) {
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