const axios = require('axios');

// Set your Together AI API key
const apiKey = "5a6ce137fb4b048a950322cc102fc58b7288952c5ee8c63b418f19c5731bfcb6";

async function getChatCompletion(message) {
    const url = 'https://api.together.xyz/v1/chat/completions';  // Adjust if needed based on API documentation

    try {
        const response = await axios.post(url, {
            model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages: [{ role: "user", content: message }]
        }, {
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            }
        });

        return response.data.choices[0].message.content; // Adjust as per actual response structure
    } catch (error) {
        console.error("Error fetching completion:", error.message);
    }
}

async function start() {
    const history = [];
    let message;

    while (true) {
        message = prompt("How can I help you today? (type 'quit' to exit):");
        
        if (message.toLowerCase() === "quit") {
            console.log("Exiting...");
            break;
        }

        history.push({ role: "user", content: message });
        const answer = await getChatCompletion(message);
        
        console.log("Together AI: ", answer);
        history.push({ role: "assistant", content: answer });
    }
}

start();
