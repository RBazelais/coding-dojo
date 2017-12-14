function RemoveAt(array, index) {
    for (var i = index; i < array.length; i++) {
        array[i] = array[i+1];
    }
    array[i].pop();
    return array;
}
RemoveAt(["a", "b", "c", "d", "e"], 3);
//TODO: Still outputs undefined at the end find out why
