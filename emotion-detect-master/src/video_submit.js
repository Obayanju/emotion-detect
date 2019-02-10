var URL = window.URL || window.webkitURL;
var video = document.getElementsByTagName('video')[0];
function onChange() {
    var fileItem = document.getElementById('fileItem');
    var files = fileItem.files;
    var file = files[0];
    var url = URL.createObjectURL(file);
    video.src = url;
    video.load();
}