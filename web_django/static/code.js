const button = document.querySelector('button');
const video = document.querySelector('video');

button.addEventListener('click', (e) => {
	navigator.mediaDevices.getUserMedia({ video: true, audio: true }).then((stream) => {
		video.srcObject = stream;
		video.play();
	}).catch((error) => {
		console.log('error', error)
	})
})

