window.addEventListener('load', registerEvents, false)

function registerEvents (event) {
  // console.log('dans registerEvents')
  // var parser = document.createElement('a')
  // parser.href = this.href
  // var cat = parser.pathname.split('/')[1]
  var navbar_active_entry = document.querySelector('.active.navbar_entry')
  navbar_active_entry.addEventListener('click', displayCategoryContent, false)

  var leftentriesList = document.querySelectorAll('a.leftentry')
  for (var i = 0; i < leftentriesList.length; ++i) {
    // console.log('dans registerEvents: ' + i)
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
  // console.log('dans displayTiles: ' + id)
  event.preventDefault()
  var parser = document.createElement('a')
  var central_content = document.getElementById('central_content')
  var all_tiles_groups = document.getElementsByClassName('tiles_group')
  parser.href = this.href
  var cat = parser.pathname.split('/')[1]
  var thm = parser.pathname.split('/')[2]
  var id = cat + '_' + thm
  var tiles_group_id = 'central_' + id
  var leftmenu_active_id = 'leftmenu_' + id

  // console.log('dans displayTiles: ' + '.leftentry.cat_' + cat)
  var all_leftmenu_entries = document.querySelectorAll('.leftentry.cat_' + cat)
  for (var i = 0; i < all_leftmenu_entries.length; ++i) {
    all_leftmenu_entries[i].classList.remove('active')
  }

  var leftmenu_active_entry = document.getElementById(leftmenu_active_id)
  leftmenu_active_entry.classList.add('active')

  fadeOut(central_content).then(function (result) {
    for (var i = 0; i < all_tiles_groups.length; ++i) {
      all_tiles_groups[i].style.display = 'none'
    }
    document.getElementById('main_content_' + cat).style.display = 'none'
    var tiles_group = document.getElementById(tiles_group_id)
    tiles_group.style.display = 'flex'
    fadeIn(central_content)
  })
  return false
}

function displayCategoryContent (event) {
  event.preventDefault()
  var parser = document.createElement('a')
  var central_content = document.getElementById('central_content')
  var all_tiles_groups = document.getElementsByClassName('tiles_group')
  parser.href = this.href
  var cat = parser.pathname.split('/')[1]

  // console.log('dans displayCategoryContent: ' + )
  var all_leftmenu_entries = document.querySelectorAll('.leftentry.cat_' + cat)
  for (var i = 0; i < all_leftmenu_entries.length; ++i) {
    all_leftmenu_entries[i].classList.remove('active')
  }

  fadeOut(central_content).then(function (result) {
    for (var i = 0; i < all_tiles_groups.length; ++i) {
      all_tiles_groups[i].style.display = 'none'
    }
    document.getElementById('main_content_' + cat).style.display = 'block'
    fadeIn(central_content)
  })
  return false
}
