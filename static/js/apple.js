var options = { responsive: true };

var ctx_donut = $("#barChart").get(0).getContext("2d");

$.get("/apple-info.json", function (data) {
    var myBarChart = new Chart(ctx_donut, {
                                            type: 'horizontalBar',
                                            data: data,
                                            options: options
                                          });
    $('#barLegend').html(myBarChart.generateLegend());
});