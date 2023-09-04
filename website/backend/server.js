const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process');
const app = express();
const PORT = 8080;

app.use(cors());
app.use(express.json());


app.get('/crawl', (req, res) => {
    try {
        console.log('Received GET request at /crawl!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!');

        // Extract input data from query parameters
        const inputData = req.query.inputData;

        // Run the Python script with input data
        runPythonSciprt(inputData);

        res.status(200).json({ message: 'Crawling started successfully' });
    } catch (error) {
        console.error('Error while handling /crawl request:', error);
        // Send an error response
        res.status(500).json({ error: 'An error occurred' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

function runPythonSciprt(inputData) {
    const pythonProcess = spawn('python', ['./search.py'], { cwd: __dirname, stdio: ['pipe', 'pipe', 'pipe'] });

    // Send input data to the Python script
    pythonProcess.stdin.write(inputData);
    pythonProcess.stdin.end();

    // Rest of the code remains the same
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