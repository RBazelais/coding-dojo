var daysUntilMyBirthday = 60;
function birthdayCountdown(){
    for (var i = daysUntilMyBirthday; i >= 1; i--){
        if(i > 30){
            console.log(i + " days until my birthday. Just get here already! uggh :(");
        }else if(i < 15 && i > 5){
            console.log(i + " days until my birthday. It's almost here! :D");
        }else if(i <= 5){
            console.log(i + " days until my birthday. It's gonna be LIT... :(");
        }else if(i === 0){
            console.log("♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*\n♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪\n*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«");
        }else{
            console.log(i + " days until my birthday. Such a long time... :(");
        }
    }
}
birthdayCountdown();
