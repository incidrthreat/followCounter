var source = new EventSource("/update");
    source.onmessage = function(event) {
        ////example 1678 followers
        //var th = Math.floor(event.data/1000); // thousands spot should be 1
        //var h = Math.floor((event.data/100)%10); // hundreds spot should be 6
        //var t = Math.floor((event.data/10)%10); // tens spot should be 7
        //var o = Math.floor(event.data%10); // ones spot should be 8
        
        //document.getElementById("thousands").textContent = th;
        //document.getElementById("hundreds").textContent = h;
        //document.getElementById("tens").textContent = t;
        //document.getElementById("ones").textContent = o;
        
        odometer.innerHTML = event.data;
        
};