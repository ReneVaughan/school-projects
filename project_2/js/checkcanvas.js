// check canvas
if(Modernizr.canvas){
	//Canvas is supported
	var theCanvas = document.getElementById("canvas");
	var ctx = theCanvas.getContext("2d");
	
	//Draw some text on our canvas
	console.log("Canvas Supported");
	
	
	}else {
		console.log("Canvas not Supported");
		
		}

	console.log(Modernizr);