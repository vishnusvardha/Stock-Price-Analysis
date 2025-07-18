


// Chart.js setup
let chart;
function renderChart(history, predicted) {
    const ctx = document.getElementById('predictionChart').getContext('2d');
    if (chart) chart.destroy();
    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: history.map((_, i) => `T-${history.length - i}` ).concat(['Prediction']),
            datasets: [{
                label: 'Stock Price',
                data: history.concat([predicted]),
                borderColor: '#6c63ff',
                backgroundColor: 'rgba(76, 110, 245, 0.08)',
                pointBackgroundColor: ctx.createLinearGradient(0,0,0,400),
                fill: true,
                tension: 0.2,
                pointRadius: function(ctx) {
                    return ctx.dataIndex === ctx.dataset.data.length-1 ? 7 : 4;
                },
                pointBackgroundColor: function(ctx) {
                    return ctx.dataIndex === ctx.dataset.data.length-1 ? '#ff4b5c' : '#6c63ff';
                },
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false },
                tooltip: { enabled: true }
            },
            scales: {
                x: { display: true, title: { display: false } },
                y: { display: true, title: { display: true, text: 'Price' } }
            }
        }
    });
}

// On submit, send only the stock symbol
document.getElementById('stockForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const symbol = document.getElementById('stockSymbol').value.trim().toUpperCase();
    if (!symbol) return;
    document.getElementById('result').innerText = 'Predicting...';
    try {
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ symbol }),
        });
        const result = await response.json();
        if (result.predicted_price !== undefined) {
            document.getElementById('result').innerText = `Predicted Stock Price for ${symbol}: $${result.predicted_price.toFixed(2)}`;
            if (result.history && Array.isArray(result.history) && result.history.length > 0) {
                renderChart(result.history, result.predicted_price);
            } else {
                renderChart([result.predicted_price], result.predicted_price);
            }
        } else if (result.error) {
            document.getElementById('result').innerText = `Error: ${result.error}`;
        } else {
            document.getElementById('result').innerText = 'Prediction: undefined';
        }
    } catch (err) {
        document.getElementById('result').innerText = 'Error: Could not connect to server.';
    }
});

