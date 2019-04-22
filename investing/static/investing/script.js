function setChart(years, carLoans, apartmentLoans, capitals, totalCapitals) {
  var ctx = $('#myChart');
  var lineTension = 0.1;
  var fill = false;
  var mixedChart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Car Loan',
            data: carLoans,
            backgroundColor: 'rgba(125, 175, 0, 0.5)',
            borderColor: 'rgba(125, 175, 0, 1)',
            fill: fill,
            lineTension: lineTension,
        }, {
            label: 'Apartment Loan',
            data: apartmentLoans,
            backgroundColor: 'rgba(200, 100, 0, 0.75)',
            borderColor: 'rgba(200, 100, 0, 1)',
            fill: fill,
            lineTension: lineTension,
        }, {
            label: 'Capital',
            data: capitals,
            backgroundColor: 'rgba(175, 125, 0, 0.75)',
            borderColor: 'rgba(175, 125, 0, 1)',
            fill: fill,
            lineTension: lineTension,
        }, {
            label: 'Total Capital',
            data: totalCapitals,
            backgroundColor: 'rgba(175, 175, 0, 0.75)',
            borderColor: 'rgba(175, 175, 0, 1)',
            fill: fill,
            lineTension: lineTension,
        }],
        labels: years
    },
    options: {}
  });
};

$(document).ready(function() {

  $.ajax({
    method: "GET",
    url: $('#myChart').attr("url"),
    success: function(data) {
      setChart(data.years, data.carLoans, data.apartmentLoans, data.capitals, data.totalCapitals);
    },
    error: function(data) {
      console.log("error!");
    }
  });


});
