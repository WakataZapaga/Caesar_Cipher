async function processMessage(action) 
{
    const message = document.getElementById('message').value;
    const shift = parseInt(document.getElementById('shift').value);

    const response = await fetch(`http://127.0.0.1:5000/${action}`, 
    {
        method: 'POST',
        headers: 
        {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message, shift })
    });

    const data = await response.json();
    document.getElementById('result').innerText = data.result;
}