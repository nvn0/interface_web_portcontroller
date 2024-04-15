function sendData() {
    var data = document.getElementById("data-input").value;

    // Enviar os dados para o servidor usando uma requisição POST
    fetch('/processar_dados', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: data })
    })
    .then(response => response.json())
    .then(data => {
        // Aqui você pode manipular a resposta do servidor, se necessário
        console.log('Resposta do servidor:', data);
    })
    .catch(error => {
        console.error('Erro ao enviar dados para o servidor:', error);
    });
}
