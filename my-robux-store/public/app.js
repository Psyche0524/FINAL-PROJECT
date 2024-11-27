document.getElementById('purchase-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const amount = document.getElementById('amount').value;

    const response = await fetch('/purchase', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, amount })
    });

    const result = await response.json();

    if (result.success) {
        alert('Purchase successful!');
    } else {
        alert('Purchase failed: ' + result.message);
    }
});
