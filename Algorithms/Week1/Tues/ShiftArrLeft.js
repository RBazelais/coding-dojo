var arrayLeft = [4, 7, 42, 1, 8, 20];
for(var i = 0; i < arrayLeft.length-1; i++){
    arrayLeft[i] = arrayLeft[i+1];
    console.log(arrayLeft);
};
arrayLeft[i] = 0;
console.log(arrayLeft);
//TODO: Still outputs undefined at the end find out why

//pop();
//push(0);
