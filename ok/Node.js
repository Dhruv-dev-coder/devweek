const axios = require('axios');
const readline = require('readline');

// Your Together AI API key
const apiKey = "5a6ce137fb4b048a950322cc102fc58b7288952c5ee8c63b418f19c5731bfcb6";

// Create an interface for reading input from the command line
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let history = [];

// Function to get chat completion from the Together AI API
async function getChatCompletion(message) {
    try {
        const response = await axios.post('https://api.together.xyz/v1/chat/completions', {
            model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages: [
                {
                    role: "user",
                    content: message
                }
            ]
        }, {
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            }
        });

        return response.data.choices[0].message.content;  // Adjust based on the API response structure
    } catch (error) {
        console.error("Error fetching completion:", error.message);
        return "I'm sorry, I couldn't process that request.";
    }
}

// Function to start the chat loop
function start() {
    rl.question("How can I help you today? (type 'quit' to exit): ", async (message) => {
        if (message.toLowerCase() === 'quit') {
            console.log("Exiting...");
            rl.close();
            return;
        }

        history.push({ role: "user", content: message });

        const answer = await getChatCompletion(message);
        console.log("Together AI: ", answer);
        history.push({ role: "assistant", content: answer });

        // Restart the chat loop
        start();
    });
}

// Start the chat
start();
