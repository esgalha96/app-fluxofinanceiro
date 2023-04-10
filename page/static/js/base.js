RenderizarGraficoEntradas = function(url){
    fetch(url)
    .then(response => response.json())
    .then(data => {
    var ctx = document.getElementById('GraficoEntradas').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
        labels: data.labels,
        datasets: [{
            label: 'Entradas por Mês',
            data: data.valores,
            backgroundColor: 'rgba(22, 112, 204, 0.3)',
            borderColor: 'rgba(22, 112, 204, 1)',
            borderWidth: 1
        }]
        },
        options: {
        scales: {
            y: {
            beginAtZero: true
            }
        }
        }
    });
    });
}

RenderizarGraficoSaidas = function(url){
    fetch(url)
    .then(response => response.json())
    .then(data => {
    var ctx = document.getElementById('GraficoSaidas').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
        labels: data.labels,
        datasets: [{
            label: 'Saídas por Mês',
            data: data.valores,
            backgroundColor: 'rgba(204, 16, 2, 0.3)',
            borderColor: 'rgba(204, 16, 2, 1)',
            borderWidth: 1
        }]
        },
        options: {
        scales: {
            y: {
            beginAtZero: true
            }
        }
        }
    });
    });
}

RenderizarGraficoFluxoCaixa = function(url){
    fetch(url)
    .then(response => response.json())
    .then(data => {
    var ctx = document.getElementById('GraficoFluxoCaixa').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
        labels: data.labels,
        datasets: [{
                    label: 'Saídas por Mês',
                    data: data.valores.saidas,
                    backgroundColor: 'rgba(204, 16, 2, 0.3)',
                    borderColor: 'rgba(204, 16, 2, 1)',
                    borderWidth: 2,
                    type:'line',

                },
                {
                    label: 'Entradas por Mês',
                    data: data.valores.entradas,
                    backgroundColor: 'rgba(22, 112, 204, 0.3)',
                    borderColor: 'rgba(22, 112, 204, 1)',
                    borderWidth: 2,
                    type:'line',

                },
                {
                    label: 'Fluxo por Mês',
                    data: data.valores.fluxo,
                    backgroundColor: 'rgba(87, 204, 0, 0.3)',
                    borderColor: 'rgba(87, 204, 0, 1)',
                    borderWidth: 1,
                    
                },
            ]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                beginAtZero: true
                }
            }
        }
    });
    });
}