$(function(){
	var canvas = document.getElementById("canvas");
	var ctx = canvas.getContext("2d");

	// Setup Graph
	var RadarData = {
		labels:["Small Birds", "Small Critters", "Deer", "Chipmunks", "Woodchucks", "Raccoons", "Owls", "Eagles", "Wolves", "Black Bears", "Other"],
		datasets:[
		{
			fillColor: "rgba(175,251,255,.5)",
			strokeColor: "rgba(175, 251, 255, 1)",
			pointColor: "rgba(175,251,255,1)",
			pointStrokeColor: "#FAFFF",
			pointHighlightFill: "#FAFFF",
			pointHighlightStroke: "rgba(175,251,255,1)",
			data:[50,13,10,7,6,5,3,2,1,1,2]
			},
			{
				fillColor: "rgba(151,187,205,0.5)",
           	strokeColor: "rgb(151,187,208)",
            	pointColor: "rgb(151,187,208)",
            	pointStrokeColor: "#707F9E",
            	pointHighlightFill: "#707F9E",
            	pointHighlightStroke: "rgb(151,187,205)",
            	data: [10,27,20,7,6,5,13,2,2,1,7]
			}
		]
	};
	// create graph
	var myLine = new Chart(ctx).Radar(RadarData);
});



