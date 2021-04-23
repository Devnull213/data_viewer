$(document).ready(function () {
  let stulzOneEndpoint = "/admin_view/stulz_one_data";
  let stulzTwoEndpoint = "/admin_view/stulz_two_data";
  let labels = [];
  let stulzOneTempData = [];
  let stulzTwoTempData = [];
  let stulzOneHumData = [];
  let stulzTwoHumData = [];

  $.ajax({
    method: "GET",
    url: stulzOneEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      stulzOneTempData = data.temp;
      stulzOneHumData = data.hum;
      var ctx = document.getElementById("stulzOneChart").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color:["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Temperatura en grados",
              data: stulzOneTempData,
              borderColor: ["rgba(255, 99, 132, 1)"],
              borderWidth: 2
            },
            {
              type: "line",
              label: "Porcentaje de humedad",
              data: stulzOneHumData,
              borderColor: ["rgba( 45, 99, 255, 1)"],
              borderWidth: 2
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Stulz #1",
            },
          },
            scales:{
                y:{
                    beginAtZero: true,
                }
            },
            responsive: true,
            mantainAspectRatio: false,
        },
      });
    },
    error: function (error_data) {
      console.log("error");
      console.log(error_data);
    },
  });

  $.ajax({
    method: "GET",
    url: stulzTwoEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      stulzTwoTempData = data.temp;
      stulzTwoHumData = data.hum;
      var ctx = document.getElementById("stulzTwoChart").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color:["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Temperatura en grados",
              data: stulzTwoTempData,
              borderColor: ["rgba(255, 99, 132, 1)"],
              borderWidth: 2
            },
            {
              type: "line",
              label: "Porcentaje de humedad",
              data: stulzTwoHumData,
              borderColor: ["rgba( 45, 99, 255, 1)"],
              borderWidth: 2
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Stulz #2",
            },
          },
            scales:{
                y:{
                    beginAtZero: true,
                }
            },
            responsive: true,
            mantainAspectRatio: false,
        },
      });
    },
    error: function (error_data) {
      console.log("error");
      console.log(error_data);
    },
  });
});