function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
    
}

function renderiza_total_vendido(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('faturamento_total').innerHTML = data.total
    })

}



function renderiza_faturamento_mensal(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('faturamento_mensal').getContext('2d');
        var cores_faturamento_mensal = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                datasets: [{
                    label: data.labels,
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
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


    })


    

}

function renderiza_despesas_mensal(resultados) {
    // Extrai os meses/anos únicos
    const mesesAnos = [...new Set(resultados.map(item => item.mes_ano))];

    // Filtra os resultados para cada loja e extrai os dados
    const dataFLN = mesesAnos.map(mesAno => resultados.find(item => item.mes_ano === mesAno && item.loj_descricao === 'FLN').soma_valorliquido || 0);
    const dataBNU = mesesAnos.map(mesAno => resultados.find(item => item.mes_ano === mesAno && item.loj_descricao === 'BNU').soma_valorliquido || 0);
    const dataPOA = mesesAnos.map(mesAno => resultados.find(item => item.mes_ano === mesAno && item.loj_descricao === 'P01').soma_valorliquido || 0);

    // Renderiza o gráfico com os dados processados
    renderizarGrafico(mesesAnos, dataFLN, dataBNU, dataPOA);
}

function renderizarGrafico(mesesAnos, dataFLN, dataBNU, dataPOA) {
    const ctx = document.getElementById('despesas_mensal').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: mesesAnos,
            datasets: [{
                label: 'FLN', // Rótulo para os dados da loja FLN
                data: dataFLN,
                backgroundColor: '#0152a1', // Cor para os dados da loja FLN
                borderColor: "#FFFFFF",
                borderWidth: 0.2
            }, {
                label: 'BNU', // Rótulo para os dados da loja BNU
                data: dataBNU,
                backgroundColor: '#e87717', // Cor para os dados da loja BNU
                borderColor: "#FFFFFF",
                borderWidth: 0.2
            }, {
                label: 'POA', // Rótulo para os dados da loja POA
                data: dataPOA,
                backgroundColor: '#4ea8ff', // Cor para os dados da loja POA
                borderColor: "#FFFFFF",
                borderWidth: 0.2
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Mês/Ano'
                    }
                }]
            },
            tooltips: {
                callbacks: {
                    label: function(tooltipItem, data) {
                        var label = data.datasets[tooltipItem.datasetIndex].label || '';
                        if (label) {
                            label += ': ';
                        }
                        label += tooltipItem.yLabel.toFixed(2);
                        return label;
                    }
                }
            }
        }
    });
}

function renderiza_funcionario_mes(url){



    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        const ctx = document.getElementById('funcionarios_do_mes').getContext('2d');
        var cores_funcionarios_do_mes = gera_cor(qtd=4)
        const myChart = new Chart(ctx, {
            type: 'polarArea',
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.data,
                    backgroundColor: cores_funcionarios_do_mes[0],
                    borderColor: cores_funcionarios_do_mes[1],
                    borderWidth: 1
                }]
            },
            
        });


    })

}