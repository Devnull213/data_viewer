$(document).ready(function () {
  let stulzOneEndpoint = "/admin_view/stulz_one_data";
  let stulzTwoEndpoint = "/admin_view/stulz_two_data";
  let carrierOneEndpoint = "/admin_view/carrier_one_data";
  let carrierTwoEndpoint = "/admin_view/carrier_two_data";
  let upsOneEndpoint = "/admin_view/ups_one_data";
  let upsTwoEndpoint = "/admin_view/ups_two_data";
  let chillerUniflairEndpoint = "/admin_view/chiller_uniflair_data";
  let chillerClimavenettaEndpoint = "/admin_view/chiller_climavenetta_data";
  let pumpOneEndpoint = "/admin_view/pump_one_data";
  let pumpTwoEndpoint = "/admin_view/pump_two_data";
  let pumpThreeEndpoint = "/admin_view/pump_three_data";
  let geOneEndpoint = "/admin_view/ge_one_data";
  let geTwoEndpoint = "/admin_view/ge_two_data";
  let PowerEndpoint = "/admin_view/power_data";
  let labels = [];
  let stulzOneTempData = [];
  let stulzTwoTempData = [];
  let stulzOneHumData = [];
  let stulzTwoHumData = [];
  let carrierOneTempData = [];
  let carrierTwoTempData = [];
  let upsOneVoltuin = [];
  let upsOneVoltvin = [];
  let upsOneVoltwin = [];
  let upsOneCurruin = [];
  let upsOneCurrvin = [];
  let upsOneCurrwin = [];
  let upsTwoVoltuin = [];
  let upsTwoVoltvin = [];
  let upsTwoVoltwin = [];
  let upsTwoCurruin = [];
  let upsTwoCurrvin = [];
  let upsTwoCurrwin = [];
  let uniflairTempIn = [];
  let uniflairTempOut = [];
  let uniflairEvapressurec1 = [];
  let uniflairEvapressurec2 = [];
  let uniflairCondpressurec1 = [];
  let uniflairCondpressurec2 = [];
  let climavenettaTempIn = [];
  let climavenettaTempOut = [];
  let climavenettaEvapressurec1 = [];
  let climavenettaEvapressurec2 = [];
  let climavenettaCondpressurec1 = [];
  let climavenettaCondpressurec2 = [];
  let pumpOnePressIn = [];
  let pumpTwoPressIn = [];
  let pumpThreePressIn = [];
  let pumpOnePressOut = [];
  let pumpTwoPressOut = [];
  let pumpThreePressOut = [];
  let geOneTemp = [];
  let geTwoTemp = [];
  let geOneVolt= [];
  let geTwoVolt= [];
  let kva = [];
  let kw = [];
  let kvar = [];
  let kva_total = [];
  let kw_total = [];
  let kvar_total = [];

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
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Temperatura en grados",
              data: stulzOneTempData,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "line",
              label: "Porcentaje de humedad",
              data: stulzOneHumData,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Stulz #1",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Temperatura en grados",
              data: stulzTwoTempData,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "line",
              label: "Porcentaje de humedad",
              data: stulzTwoHumData,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Stulz #2",
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: carrierOneEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      carrierOneTempData = data.temp;
      var ctx = document.getElementById("carrierOneChart").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Temperatura en grados",
              data: carrierOneTempData,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Carrier #1",
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: carrierTwoEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      carrierTwoTempData = data.temp;
      var ctx = document.getElementById("carrierTwoChart").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Temperatura en grados",
              data: carrierTwoTempData,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Carrier #2",
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: upsOneEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      upsOneVoltuin = data.volt_u_in;
      upsOneVoltvin = data.volt_v_in;
      upsOneVoltwin = data.volt_w_in;
      upsOneCurruin = data.curr_u_in;
      upsOneCurrvin = data.curr_v_in;
      upsOneCurrwin = data.curr_w_in;
      var ctx = document.getElementById("upsOneChartIn").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "bar",
              label: "Voltaje linea U ",
              data: upsOneVoltuin,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Voltaje linea V",
              data: upsOneVoltvin,
              borderColor: ["rgba( 236, 57, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Voltaje linea W",
              data: upsOneVoltwin,
              borderColor: ["rgba( 236, 111, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea U ",
              data: upsOneCurruin,
              borderColor: ["rgba(11, 55, 220, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea V",
              data: upsOneCurrvin,
              borderColor: ["rgba(11, 123, 220, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea W",
              data: upsOneCurrwin,
              borderColor: ["rgba(11, 180, 220, 1)"],
              borderWidth: 3,
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Entrada UPS #1",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: upsOneEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      upsOneVoltuout = data.volt_u_out;
      upsOneVoltvout = data.volt_v_out;
      upsOneVoltwout = data.volt_w_out;
      upsOneCurruout = data.curr_u_out;
      upsOneCurrvout = data.curr_v_out;
      upsOneCurrwout = data.curr_w_out;
      var ctx = document.getElementById("upsOneChartOut").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "bar",
              label: "Voltaje linea U ",
              data: upsOneVoltuout,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Voltaje linea V",
              data: upsOneVoltvout,
              borderColor: ["rgba( 236, 57, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Voltaje linea W",
              data: upsOneVoltwout,
              borderColor: ["rgba( 236, 111, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea U ",
              data: upsOneCurruout,
              borderColor: ["rgba(11, 55, 220, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea V",
              data: upsOneCurrvout,
              borderColor: ["rgba(11, 123, 220, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea W",
              data: upsOneCurrwout,
              borderColor: ["rgba(11, 180, 220, 1)"],
              borderWidth: 3,
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Salida UPS #1",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: upsTwoEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      upsTwoVoltuin = data.volt_u_in;
      upsTwoVoltvin = data.volt_v_in;
      upsTwoVoltwin = data.volt_w_in;
      upsTwoCurruin = data.curr_u_in;
      upsTwoCurrvin = data.curr_v_in;
      upsTwoCurrwin = data.curr_w_in;
      var ctx = document.getElementById("upsTwoChartIn").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "bar",
              label: "Voltaje linea U ",
              data: upsTwoVoltuin,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Voltaje linea V",
              data: upsTwoVoltvin,
              borderColor: ["rgba( 236, 57, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Voltaje linea W",
              data: upsTwoVoltwin,
              borderColor: ["rgba( 236, 111, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea U ",
              data: upsTwoCurruin,
              borderColor: ["rgba(11, 55, 220, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea V",
              data: upsTwoCurrvin,
              borderColor: ["rgba(11, 123, 220, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea W",
              data: upsTwoCurrwin,
              borderColor: ["rgba(11, 180, 220, 1)"],
              borderWidth: 3,
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Entrada UPS #2",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: upsTwoEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      upsTwoVoltuout = data.volt_u_out;
      upsTwoVoltvout = data.volt_v_out;
      upsTwoVoltwout = data.volt_w_out;
      upsTwoCurruout = data.curr_u_out;
      upsTwoCurrvout = data.curr_v_out;
      upsTwoCurrwout = data.curr_w_out;
      var ctx = document.getElementById("upsTwoChartOut").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "bar",
              label: "Voltaje linea U ",
              data: upsTwoVoltuout,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Voltaje linea V",
              data: upsTwoVoltvout,
              borderColor: ["rgba( 236, 57, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Voltaje linea W",
              data: upsTwoVoltwout,
              borderColor: ["rgba( 236, 111, 3, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea U ",
              data: upsTwoCurruout,
              borderColor: ["rgba(11, 55, 220, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea V",
              data: upsTwoCurrvout,
              borderColor: ["rgba(11, 123, 220, 1)"],
              borderWidth: 3,
            },
            {
              type: "bar",
              label: "Corriente linea W",
              data: upsTwoCurrwout,
              borderColor: ["rgba(11, 180, 220, 1)"],
              borderWidth: 3,
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Salida UPS #2",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: chillerUniflairEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      uniflairTempIn = data.temp_in;
      uniflairTempOut = data.temp_out;
      var ctx = document
        .getElementById("chillerUniflairChart")
        .getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Temperatura de entrada en grados",
              data: uniflairTempIn,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "line",
              label: "Temperatura de salida en grados",
              data: uniflairTempOut,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Temperatura entrada y salida Chiller Uniflair",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: chillerUniflairEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      uniflairEvapressurec1 = data.eva_pressure_c1;
      uniflairEvapressurec2 = data.eva_pressure_c2;
      uniflairCondpressurec1 = data.cond_pressure_c1;
      uniflairCondpressurec2 = data.cond_pressure_c2;
      var ctx = document
        .getElementById("chillerUniflairPressure")
        .getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "bar",
              label: "Presión de evaporación circuito uno",
              data: uniflairEvapressurec1,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "bar",
              label: "Presión de evaporación circuito dos",
              data: uniflairEvapressurec2,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "bar",
              label: "Presión de condensación circuito uno",
              data: uniflairCondpressurec1,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
            {
              type: "bar",
              label: "Presión de condensación circuito dos",
              data: uniflairCondpressurec2,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Temperatura entrada y salida Chiller Uniflair",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: chillerClimavenettaEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      climavenettaTempIn = data.temp_in;
      climavenettaTempOut = data.temp_out;
      var ctx = document
        .getElementById("chillerClimavenettaChart")
        .getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Temperatura de entrada en grados",
              data: climavenettaTempIn,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "line",
              label: "Temperatura de salida en grados",
              data: climavenettaTempOut,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Temperatura entrada y salida Chiller Climavenetta",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: chillerClimavenettaEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      climavenettaEvapressurec1 = data.eva_pressure_c1;
      climavenettaEvapressurec2 = data.eva_pressure_c2;
      climavenettaCondpressurec1 = data.cond_pressure_c1;
      climavenettaCondpressurec2 = data.cond_pressure_c2;
      var ctx = document
        .getElementById("chillerClimavenettaPressure")
        .getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "bar",
              label: "Presión de evaporación circuito uno",
              data: climavenettaEvapressurec1,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "bar",
              label: "Presión de evaporación circuito dos",
              data: climavenettaEvapressurec2,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "bar",
              label: "Presión de condensación circuito uno",
              data: climavenettaCondpressurec1,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
            {
              type: "bar",
              label: "Presión de condensación circuito dos",
              data: climavenettaCondpressurec2,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Temperatura entrada y salida Chiller Climavenetta",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: pumpOneEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      pumpOnePressIn = data.pressure_in;
      pumpOnePressOut = data.pressure_out;
      var ctx = document.getElementById("pumpOneChart").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Presión de bombeo",
              data: pumpOnePressOut,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "line",
              label: "Presión de retorno",
              data: pumpOnePressIn,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Bomba #3",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: pumpTwoEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      pumpTwoPressIn = data.pressure_in;
      pumpTwoPressOut = data.pressure_out;
      var ctx = document.getElementById("pumpTwoChart").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Presión de Bombeo",
              data: pumpTwoPressOut,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "line",
              label: "Presión de retorno",
              data: pumpTwoPressIn,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Bomba #2",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: pumpThreeEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      pumpThreePressIn = data.pressure_in;
      pumpThreePressOut = data.pressure_out;
      var ctx = document.getElementById("pumpThreeChart").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Presión de bombeo",
              data: pumpThreePressOut,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "line",
              label: "Presión de retorno",
              data: pumpThreePressIn,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Bomba #3",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: geOneEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      geOneTemp = data.temp;
      geOneVolt= data.volt;
      var ctx = document.getElementById("geOneChart").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Temperatura en grados",
              data: geOneTemp,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "line",
              label: "Voltaje",
              data: geOneVolt,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Grupo electrógeno C15",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: geTwoEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      geTwoTemp = data.temp;
      geTwoVolt= data.volt;
      var ctx = document.getElementById("geTwoChart").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "Temperatura en grados",
              data: geTwoTemp,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "line",
              label: "Voltaje",
              data: geTwoVolt,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Grupo electrógeno C15",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: PowerEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      kva = data.kva;
      kw = data.kw;
      kvar = data.kvar;
      var ctx = document.getElementById("powerChart").getContext("2d");
      var myChart = new Chart(ctx, {
        backgroundColor: ["rgba(34, 33, 36, 1)"],
        color: ["rgba(255, 255, 255, 1)"],
        data: {
          labels: labels,
          datasets: [
            {
              type: "line",
              label: "KVA",
              data: kva,
              borderColor: ["rgba(236, 3, 3, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba(236, 3, 3, 0.1)"],
            },
            {
              type: "line",
              label: "KW",
              data: kw,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
            {
              type: "line",
              label: "KVAR",
              data: kvar,
              borderColor: ["rgba( 29, 224, 245, 1)"],
              borderWidth: 3,
              fill: true,
              backgroundColor: ["rgba( 29, 224, 245, 0.1)"],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Potencia Tablero general",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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
    url: PowerEndpoint,
    success: function (data) {
      console.log(data);
      labels = data.labels;
      kva_total.push(data.kva_total);
      kva_total.push(data.kw_total);
      kva_total.push(data.kvar_total);
      var ctx = document.getElementById("powerPromChart").getContext("2d");
      var myChart = new Chart(ctx, {
        data: {
          labels: ['KVA', 'KW', 'KVAR'],
          datasets: [
            {
              type: "polarArea",
              label: ['Potencia de la instalación'],
              data: kva_total,
              borderColor: [
                "rgba(11, 55, 220, 1)",
                "rgba(11, 133, 220, 1)",
                "rgba(11, 180, 220, 1)",
              ],
              borderWidth: 3,
              fill: true,
              backgroundColor: [
                "rgba(11, 55, 220, 0.4)",
                "rgba(11, 133, 220, 0.4)",
                "rgba(11, 180, 220, 0.4)",
              ],
            },
          ],
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Potencia Tablero general",
              fontSize: 30,
            },
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 15,
                borderWidth: 15,
              },
            },
          },
          elements: {
            point: {
              radius: 4,
              borderWidth: 2,
              backgroundColor: "white",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
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

$(document).ready(function () {
  // $('#bombas').hide();
  $("#bombas-trigger").click(function () {
    $("#bombas").fadeIn();
  });

});
