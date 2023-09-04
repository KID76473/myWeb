const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process'); // Import the spawn function
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

        // Run the Python script
        runPythonScript();

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

// Function to run the Python script
function runPythonScript() {
    const pythonProcess = spawn('python', ['your_python_script.py'], { cwd: __dirname });

    pythonProcess.stdout.on('data', (data) => {
        console.log(`Python script output: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error from Python script: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python script exited with code ${code}`);
    });
}

// Replace 'your_python_script.py' with the actual name of your Python file
