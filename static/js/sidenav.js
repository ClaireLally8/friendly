$(document).ready(function() {
	const hamburgerBtn = document.getElementById('hamburgerBtn');
	hamburgerBtn.addEventListener('click', function open () {
        sidemenunav.classList.toggle('open');
	});
});