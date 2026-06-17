const API_BASE = '/api'



function getToken() {
    return localStorage.getItem('access_token')
}



async function apiFetch(endpoint, options = {}){

    const token = getToken();

    if (!token) {
        window.location.href = '/login/';
        return;
    }

    const response = await fetch(`${API_BASE}${endpoint}`, {
        ...options,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
            ...options.headers,
        }
    });

    if(response.status === 401){
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        window.location.href = '/login/';
        return;
    }

    return response;
}


function logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    window.location.href = '/login/';
}