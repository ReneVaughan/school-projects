function validateFunction(){
var errorMsg = "";
var weightCheck = document.getElementById('weight').value;
var minuteCheck = document.getElementById('minutes').value;

if (weightCheck === ""){
    errorMsg += alert("Weight needs to be filled in.");
}else{
	 console.log("ok");
}

if (minuteCheck ===''){
    errorMsg += alert("Minutes needs to be filled in.");
}else{
    console.log("ok");
}


