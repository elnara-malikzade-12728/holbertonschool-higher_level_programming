const clickableElement = document.querySelector('#red_header');
const header = document.querySelector('header');

function changeColor()
{
  header.style.color = '#FF0000';
}
clickableElement.addEventListener('click', changeColor);