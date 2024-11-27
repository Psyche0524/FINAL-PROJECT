const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = 3000;

app.use(bodyParser.json());
app.use(express.static('public'));

app.post('/purchase', (req, res) => {
    const { username, amount } = req.body;

    // Simulate a purchase process
    if (username && amount) {
        // Add your logic here (e.g., interacting with the payment gateway)
        res.json({ success: true });
    } else {
        res.json({ success: false, message: 'Invalid input' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
