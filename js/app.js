const constraints = {
  video: true
};

const video = document.querySelector("video");

function hasGetUserMedia() {
  return !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
}
if (hasGetUserMedia()) {
  navigator.mediaDevices
    .getUserMedia(constraints)
    .then(stream => (video.srcObject = stream));
} else {
  alert("getUserMedia() is not supported by your browser");
}
