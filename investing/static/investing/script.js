function setChart(years, carLoans, capitals, totalCapitals) {
  var ctx = $('#myChart');
  var mixedChart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Car Loan',
            data: carLoans,
            backgroundColor: 'rgba(125, 175, 0, 0.5)',
            borderColor: 'rgba(125, 175, 0, 1)',
            fill: false,
            lineTension: 0.1,
        }, {
            label: 'Capital',
            data: capitals,
            backgroundColor: 'rgba(175, 125, 0, 0.75)',
            borderColor: 'rgba(175, 125, 0, 1)',
            fill: false,
            lineTension: 0.1,
        }, {
            label: 'Total Capital',
            data: totalCapitals,
            backgroundColor: 'rgba(175, 175, 0, 0.75)',
            borderColor: 'rgba(175, 175, 0, 1)',
            fill: false,
            lineTension: 0.1,
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
      setChart(data.years, data.carLoans, data.capitals, data.totalCapitals);
    },
    error: function(data) {
      console.log("error!");
    }
  });


});
