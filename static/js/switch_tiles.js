window.addEventListener('load', registerEvents, false)

function registerEvents (event) {
  console.log('dans registerEvents')
  var leftentriesList = document.querySelectorAll('a.leftentry')
  for (var i = 0; i < leftentriesList.length; ++i) {
    console.log('dans registerEvents: ' + i)
    leftentriesList[i].addEventListener('click', displayTiles, false)
  }
  // document.getElementById('leftmenu_4e_equations').addEventListener('click', displayTiles, false)
}

function fadeOut (el) {
  return new Promise(function (resolve, reject) {
    el.style.opacity = 1

    ;(function fade () {
      if ((el.style.opacity -= 0.1) < 0) {
        el.style.display = 'none'
        resolve(true)
      } else {
        // console.log('dans fade(out): ' + el.style.opacity)
        window.requestAnimationFrame(fade)
      }
    })()
  })
}

function fadeIn (el, display) {
  el.style.opacity = 0
  el.style.display = display || 'block'

  ;(function fade () {
    var val = parseFloat(el.style.opacity)
    // console.log('dans fade(in): ' + val)
    // console.log('dans fade(in): ' + !((val += 0.1) > 1))
    if (!((val += 0.1) > 1)) {
      el.style.opacity = val
      window.requestAnimationFrame(fade)
    }
  })()
}

function displayTiles (event) {
  console.log('dans displayTiles: ' + id)
  event.preventDefault()
  var parser = document.createElement('a')
  var central_content = document.getElementById('central_content')
  var all_tiles_groups = document.getElementsByClassName('tiles_group')
  parser.href = this.href
  var cat = parser.pathname.split('/')[1]
  var thm = parser.pathname.split('/')[2]
  var id = 'central_' + cat + '_' + thm

  fadeOut(central_content).then(function (result) {
    for (var i = 0; i < all_tiles_groups.length; ++i) {
      all_tiles_groups[i].style.display = 'none'
    }
    document.getElementById('main_content_' + cat).style.display = 'none'
    var tiles_group = document.getElementById(id)
    tiles_group.style.display = 'flex'
    fadeIn(central_content)
  })

  return false
}
