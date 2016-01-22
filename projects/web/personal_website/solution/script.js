// Add your scripts here

function greeting(){
    // alert('Hello World');
    $('.hidden').toggle();
}

function post(){
    var comment = $('#comment').val();
    $('#comments').append(comment);
}
