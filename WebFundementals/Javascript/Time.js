var HOUR = 12;
var MINUTE = 17;
var PERIOD = "PM";

function whatTimeIsIt (HOUR, MINUTE, PERIOD){
    var timeOfDay = "";

    if (PERIOD === "AM"){
        timeOfDay = "morning.";
    }else if (PERIOD === "PM") {
        timeOfDay = "evening.";
    }if (HOUR < 5 && HOUR > 12 && PERIOD === "PM"){
        timeOfDay = "afternoon.";
    }else{
        timeOfDay = PERIOD;
    }

    if (MINUTE < 15 ){
        console.log("It's just after " + HOUR + " in the " + timeOfDay);
    }else if (MINUTE === 15 ){
        console.log("It's a quarter after " + HOUR + " in the " + timeOfDay);
    }else if (MINUTE === 30) {
        console.log("It's half past " + (HOUR) + ".");
    }else if (MINUTE < 30) {
        console.log("It's almost " + HOUR + ":" + MINUTE + " in the " + timeOfDay);
    }else if (MINUTE > 30) {
        console.log("It's almost " + (HOUR++) + " in the " + timeOfDay);
    }else if (HOUR === 12 && (PERIOD === "PM" || PERIOD === "evening.")) {
        console.log("It's almost " + (HOUR++) + " in the " + timeOfDay);
    }else if (HOUR === 12 && (PERIOD === "AM" || PERIOD === "morning.")){
        console.log("It's midnight.");
    }else{
        console.log("It's " + HOUR + ":" + MINUTE + timeOfDay);
    }
}

whatTimeIsIt(HOUR, MINUTE, PERIOD);
