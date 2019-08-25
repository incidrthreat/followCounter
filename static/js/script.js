var source = new EventSource("/update");
    source.onmessage = function(event) {   
        odometer.innerHTML = event.data;
        
};

var source = new EventSource("/tweets");
    source.onmessage = function(event) {
        num_tweets.innerHTML = event.data;
        
};

var source = new EventSource("/likes");
    source.onmessage = function(event) {
        num_likes.innerHTML = event.data;
        
};