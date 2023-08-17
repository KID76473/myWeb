const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 8081;

app.use(cors());
app.use(express.json());


app.post('/crawl', (req, res) => {
    try {
        console.log('Received POST request at /crawl');

        // Extract any necessary data from the request body
        const requestData = req.body;

        // Perform the crawling operation using requestData
        const crawledData = performCrawling(requestData);

        // Send back the crawled data as the response
        res.json({ data: crawledData });
    } catch (error) {
        console.error('Error while handling /crawl request:', error);
        // Send an error response
        res.status(500).json({ error: 'An error occurred' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});
