$(document).ready(function(){
//Glow effect
$("#brand").hover(function() {
	$("#brand").removeClass('glowMe');
	$(this).addClass('glowMe');
});
$("#home").hover(function() {
	$("#home").removeClass('glowMe');
	$(this).addClass('glowMe');
});
$("#about").hover(function() {
	$("#about").removeClass('glowMe');
	$(this).addClass('glowMe');
});
$("#dev").hover(function() {
	$("#dev").removeClass('glowMe');
	$(this).addClass('glowMe');
});
$("#vid").hover(function() {
	$("#vid").removeClass('glowMe');
	$(this).addClass('glowMe');
});
$("#gal").hover(function() {
	$("#gal").removeClass('glowMe');
	$(this).addClass('glowMe');
});
// Fade
$("#brand").click(function() {
	$("#brand").fadeIn("slow");
});
$("#home").click(function() {
	$("#home").fadeIn("slow");
});
$("#about").click(function() {
	$("#about").fadeIn("slow");
});
$("#dev").click(function() {
	$("#canvas").fadeIn(3000);
});
$("#vid").click(function() {
	$("#vid").fadeIn("slow");
});
$("#gal").click(function() {
	$("#gal").fadeIn("slow");
});
)};