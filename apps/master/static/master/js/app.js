
$(document).ready(function () {

    let endpoint = '/admin_view/stulz_one_data'
    let labels = [];
    let tempData= [];
    let humData= [];

    $.ajax({
        method:'GET',
        url: endpoint,
        success: function(data){
            console.log(data);
            labels = data.labels;
            tempData = data.temp;
            humData = data.hum;
            var ctx = document.getElementById('myChart').getContext('2d');
            var myChart = new Chart(ctx, {
                data: {
                    labels: labels,
                    datasets: [{
                        type: 'line',
                        label: 'Temperatura',
                        data: tempData,
                    borderColor: [
                        'rgba(255, 99, 132, 1)']
                    },
                    {type: 'line',
                    label: 'Humedad',
                    data: humData,
                    borderColor: [
                        'rgba( 45, 99, 255, 1)']
                }],
               } 
            })},
        error: function(error_data){
            console.log('error')
            console.log(error_data)
        }
    });

});

// var ctx = document.getElementById('myChart').getContext('2d');
// var myChart = new Chart(ctx, {
//     type: 'line',
//     data: {
//         labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
//         datasets: [{
//             label: '# of Votes',
//             data: [12, 19, 3, 5, 2, 3],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
//                 'rgba(153, 102, 255, 0.2)',
//                 'rgba(255, 159, 64, 0.2)'
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(75, 192, 192, 1)',
//                 'rgba(153, 102, 255, 1)',
//                 'rgba(255, 159, 64, 1)'
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true
//             }
//         }
//     }
// });
