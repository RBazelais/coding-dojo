var money = 0.01;

function AFewBillon (){
    for(var i = 1; i <= 30; i++){
        console.log("Day " + i + ": $" + money);
        money = money*2;

        // if (money > 10000){
        //     console.log("It took " + i + "Days to reach $10,000");
        // }else if(money > 1000000){
        //     console.log("It took " + i + "Days to reach $1,000,000");
        // }else{
        //     continue;
        // }
    }

}

AFewBillon();
