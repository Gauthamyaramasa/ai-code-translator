document.addEventListener('DOMContentLoaded', () => {
    const apiKeyInput = document.getElementById('apiKey');
    const modelSelect = document.getElementById('modelSelect');
    const translateButton = document.getElementById('translateButton');
    const inputLanguage = document.getElementById('inputLanguage');
    const outputLanguage = document.getElementById('outputLanguage');
    const inputCode = document.getElementById('inputCode');
    const outputCode = document.getElementById('outputCode');

    // Toggle API key visibility
    document.getElementById('toggleApiKeyVisibility').addEventListener('click', function () {
        if (apiKeyInput.type === 'password') {
            apiKeyInput.type = 'text';
            this.textContent = '🙈';
        } else {
            apiKeyInput.type = 'password';
            this.textContent = '👁️';
        }
    });

    // Send API key to backend
    apiKeyInput.addEventListener('blur', () => {
        fetch('http://127.0.0.1:5000/set-api-key', {  // Ensure the URL matches the backend server URL
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ api_key: apiKeyInput.value })
        }).catch(error => console.error('Error:', error));
    });

    // Send model selection to backend
    modelSelect.addEventListener('change', () => {
        fetch('http://127.0.0.1:5000/set-model', {  // Ensure the URL matches the backend server URL
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ model_name: modelSelect.value })
        }).catch(error => console.error('Error:', error));
    });

    // Handle translate button click
    translateButton.addEventListener('click', () => {
        console.log('Clicked on translate button');
        const data = {
            input_code: inputCode.value,
            input_lang: inputLanguage.value,
            output_lang: outputLanguage.value
        };

        console.log('Translating the text');
        fetch('http://127.0.0.1:5000/convert-code', {  // Ensure the URL matches the backend server URL
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (result.converted_code) {
                outputCode.value = result.converted_code;
            } else {
                outputCode.value = `Error: ${result.error}`;
            }
            console.log('All processes done');
        })
        .catch(error => console.error('Error:', error));
    });
});
