document.addEventListener('keydown', function(event) {
	if (event.keyCode === 39) { // 39 is the key code for the right arrow key
	  let checkTimer = document.getElementsByClassName('fp-elapsed')[0].textContent;
	  let hour = 0;
	  let minute = 0;
	  let second = 0;
	  checkTimer = checkTimer.split(':');
	  if(checkTimer.length == 3){
		  hour = parseInt(checkTimer[0]);
		  minute = parseInt(checkTimer[1]);
		  second = parseInt(checkTimer[2]);
		  minute *= 60;
		  hour *= 3600;
		  second = second + minute + hour;
	  } else { 
		  minute = parseInt(checkTimer[0]);
		  second = parseInt(checkTimer[1]);
		  minute *= 60;
		  second = second + minute;
	  }
	  second = second+4; //앞으로 ?초 만큼(현재 4초)
	  playBookmark(second);
	}
  if (event.keyCode === 37) { 
	  let checkTimer = document.getElementsByClassName('fp-elapsed')[0].textContent;
	  let hour = 0;
	  let minute = 0;
	  let second = 0;
	  checkTimer = checkTimer.split(':');
	  if(checkTimer.length == 3){
		  hour = parseInt(checkTimer[0]);
		  minute = parseInt(checkTimer[1]);
		  second = parseInt(checkTimer[2]);
		  minute *= 60;
		  hour *= 3600;
		  second = second + minute + hour;
	  } else {
		  minute = parseInt(checkTimer[0]);
		  second = parseInt(checkTimer[1]);
		  minute *= 60;
		  second = second + minute;
	  }
	  second = second-4; //뒤로 ?초 만큼(현재 4초)
	  playBookmark(second);
	}
	  
  });