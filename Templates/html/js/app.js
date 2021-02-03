var like = d3.select("#like");
        
var dislike = d3.select("#dislike");

var other = d3.select("#other");

like.on("click", function() {
    document.getElementsByClassName("result").value = "Positive"
})

dislike.on("click", function() {
    document.getElementsByClassName("result").value = "Negative"
})

other.on("click", function() {
    document.getElementsByClassName("result").value = "Neutral"
})

var button = d3.select(".button");

var form = d3.select(".feedback");

form.on("click", function() {
    document.getElementsByClassName()
})