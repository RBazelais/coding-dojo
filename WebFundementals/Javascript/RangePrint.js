function printRange(start, end, skip){
    for (var i = 0; i <= end; i++){
        console.log(start);
        start = start + skip;
        if( start >= end){
            break;
        }
    }
}
printRange(2, 10, 2);
console.log(13 % 3);
