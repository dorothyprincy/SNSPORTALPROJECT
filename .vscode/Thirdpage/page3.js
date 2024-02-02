const left = document.querySelector(".left");
const right = document.querySelector(".right");
const container = document.querySelector(".container");

left.addEventListener("mouseenter", () => {
  container.classList.add("hover-left");
});

left.addEventListener("mouseleave", () => {
  container.classList.remove("hover-left");
});

right.addEventListener("mouseenter", () => {
  container.classList.add("hover-right");
});

right.addEventListener("mouseleave", () => {
  container.classList.remove("hover-right");
});

const dropdowns = document.querySelectorAll('.dropdown');
dropdowns.forEach(dropdown=>{
   const select = dropdown.querySelector('.select');
   const caret = dropdown.querySelector('.caret');
   const menu = dropdown.querySelector('.menu');
   const option = dropdown.querySelector('.menu li');
   const selected = dropdown.querySelector('.selected');
   select.addEventListener('click',()=>{
     select.classList.toggle('select-clicked');
     select.classList.toggle('caret-rotate');
     select.classList.toggle('menu-open');
   });  
   
`function getName(){``return "Permission";``}`
`function getName(){``return "Leave";``}`
   
    });