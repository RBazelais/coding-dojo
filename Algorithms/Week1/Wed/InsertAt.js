//Write a function that inserts a "val" at any "idx/index" of the "arr/array"

function InsertAt(array, index, val){
	for(var i = index; i < array.length; i++){
		array[i] = array[i + 1];
	}
	array[0] = array[val];
	return array;
}

InsertAt([1, 2, 3, 4, 5], 3, 6);
//TODO: Still outputs undefined at the end find out why
