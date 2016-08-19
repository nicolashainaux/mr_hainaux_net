window.addEventListener('load', unhideWrapper, false)

function unhideWrapper (event) {
  document.querySelector('#no-js').style.display = 'none'
  document.querySelector('.wrapper').style.display = 'flex'
}
