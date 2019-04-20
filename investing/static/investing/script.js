function setChart(years, carLoans, capitals) {
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
        }, {
            label: 'Capital',
            data: capitals,
            backgroundColor: 'rgba(175, 125, 0, 0.75)',
            borderColor: 'rgba(175, 125, 0, 1)',
            fill: false,
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
      setChart(data.years, data.carLoans, data.capitals);
    },
    error: function(data) {
      console.log("error!");
    }
  });


})
year
