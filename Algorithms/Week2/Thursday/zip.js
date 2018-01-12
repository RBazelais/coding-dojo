function zip(array1, array2){
    var zipped={};
    var key;
    var values;
    if(array1.length < array2.length){
        key = array2;
        values = array1;
    }else{
        key = array1;
        values= array2;
    }

    for (var i = 0; i < key.length; i++) {
        if(!zipped[key[i]]){
            zipped[key[i]] = values[i];
        }
    }

    return zipped;
}
