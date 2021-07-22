//================ Start PreLoader ================
const ld=document.querySelector('#loader');
function stopp(){
	ld.style.display='none';
	console.log("Loaded");
}
//================ End PreLoader ================


//================ Start Navigation ================
const burger=document.querySelector(".burger");
const nav=document.querySelector(".nav_right");
const rm_nav=document.querySelector(".rm_nav");

 // for sliding navbar
burger.addEventListener('click', navSlide);  
rm_nav.addEventListener('click', navSlide);

function navSlide(){
	nav.classList.toggle('nav_active');
	burger.classList.toggle('toggle');
}


//================ End Navigations ================
