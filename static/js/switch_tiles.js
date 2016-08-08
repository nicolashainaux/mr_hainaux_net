window.addEventListener('load', registerEvents, false)

function registerEvents (event) {
  console.log('dans registerEvents')
  // var leftentries_list = document.querySelectorAll('')
  document.getElementById('leftmenu_4e_equations').addEventListener('click', displayTiles, false)
}

function displayTiles (event) {
  event.preventDefault()
  console.log('dans displayTiles')
  // var computedDisplay = window.getComputedStyle(event.target).getPropertyValue('display')
  document.getElementById('main_content_4e').style.display = 'none'
  console.log('dans displayTiles 2')
  document.getElementById('content_4e_equations').style.display = 'flex'
  console.log('dans displayTiles 3')
  return false
}
