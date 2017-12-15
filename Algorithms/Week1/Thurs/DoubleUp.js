//["a",4, "d"]

function doubleUp(arr){
    /*
    var newArr=[];
        for (var i = 0; i < array.length; i++) {
        newArr.push(arr[i]);
        newArr.push(arr[i]);
        console.log(newArr);
    } */

    var originalLength = arr.length;
    arr.length = arr.length * 2;
    console.log(arr);

    for (var i = originalLength -1; i >= 0; i--) {
        arr[i * 2] = arr[i];
        arr[i*2+1] = arr[i];
        console.log(arr);
    }
    console.log("done");
}

doubleUp(['a', 'b', 'c']);

// 0 1 2
//["a", "b", "c"]

//add to index * 2
//add to index * 2 + 1

// 0 1 2 3 4 5
//[a,a,b,b,c,c]
