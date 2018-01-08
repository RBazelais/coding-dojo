$(document).ready(function(){
    console.log("document loaded~");

    $( ".btn" ).on("click", function() {
        $("p").addClass("red");
        console.log("add class was clicked");
    });
});
