window.addEventListener('load', registerEvents, false)

function registerEvents (event) {
  var mmButtons = document.querySelectorAll('.btn-mm')
  for (var i = 0; i < mmButtons.length; ++i) {
    mmButtons[i].addEventListener('click', loadFile, false)
  }
}

function releaseButtons () {
  // console.log('[releaseButtons]: ' + Date.now())
  var mmButtons = document.querySelectorAll('.btn-mm')
  for (var i = 0; i < mmButtons.length; ++i) {
    mmButtons[i].removeAttribute('disabled')
  }
  var msg = document.querySelector('#failed-creation')
  if ((typeof msg !== 'undefined') && (msg !== null)) {
    msg.parentNode.removeChild(msg)
  }
  var pressedButton = document.querySelector('.unfaded')
  if (typeof pressedButton !== 'undefined' && (pressedButton !== null)) {
    pressedButton.innerHTML = '<img src="/static/pics/colored_blocks40.png" alt="Créer" height="40" width="40">'
    pressedButton.classList.remove('unfaded')
    // pressedButton.removeAttribute('disabled')
  }
}

function loadFile (event) {
  event.preventDefault()
  var lockDuration = 10000
  // console.log('[loadFile]: this.getAttribute("href") = ' + this.getAttribute('href'))
  // console.log('[loadFile]: event.target = ' + event.target)
  var request = new XMLHttpRequest()
  var pressedButton = this
  // unfocus button:
  pressedButton.blur()
  pressedButton.innerHTML = '<img src="/static/pics/colored_moving_blocks40_o.gif" alt="Creation..." height="40" width="40">'
  // disable all buttons
  var mmButtons = document.querySelectorAll('.btn-mm')
  for (var i = 0; i < mmButtons.length; ++i) {
    mmButtons[i].setAttribute('disabled', 'disabled')
  }
  pressedButton.classList.add('unfaded')
  var url = pressedButton.getAttribute('href')
  if (pressedButton.hasAttribute('radio_id')) {
    // console.log('radio_id trouvé')
    var f = document.getElementById(pressedButton.getAttribute('radio_id'))
    var radioButtons = f.children
    for (var j = 0; j < radioButtons.length; ++j) {
      if (radioButtons[j].tagName === 'INPUT') {
        if (!radioButtons[j].hasAttribute('value')) {
          console.log('Found an <input> without value!')
        } else {
          // console.log(radioButtons[j].tagName + ': ' + radioButtons[j].value + ' >>> ' + radioButtons[j].checked)
          if (radioButtons[j].checked) {
            url = radioButtons[j].value
            // console.log('Changed url')
          }
        }
      }
    }
  }
  // Create a link object that will be used in fact to parse the url
  // in order to get the file name
  var parser = document.createElement('a')
  parser.href = url
  // var sheetName = parser.pathname.split('/')[2]
  var pdfFileName = parser.pathname.split('/')[3]
  // console.log('[loadFile]: sheetName / pdfFileName = ' + sheetName + ' / ' + pdfFileName)
  request.open('GET', url, true)
  request.responseType = 'blob'
  var tileBody = pressedButton.parentNode.parentNode
  request.onload = function () {
    // console.log('[loadFile.onload]: this.status = ' + this.status)
    if (this.status === 200) {
      // `blob` response
      // console.log(this.response)
      // create `objectURL` of `this.response` : `.pdf` as `Blob`
      var file = window.URL.createObjectURL(this.response)
      var a = document.createElement('a')
      a.href = file
      a.download = pdfFileName + '.pdf'
      document.body.appendChild(a)
      a.click()
      document.body.removeChild(a)
      pressedButton.innerHTML = '<img src="/static/pics/lock.gif" alt="Veuillez patienter..." height="40" width="40">'
      // useless and not working:
      // remove `a` following `Save As` dialog,
      // once `window` regains `focus`
      // window.onfocus = function () {
      //   document.body.removeChild(a)
      // }
    } else if (this.status === 429) {
      pressedButton.innerHTML = '<img src="/static/pics/lock.gif" alt="Veuillez patienter..." height="40" width="40">'
      tileBody.innerHTML += '<div  id="failed-creation" class="panel panel-default" style="padding: 0; margin: 0; width: 100%;"><div class="panel-body" style="background: #ffe6d5; color: #d45500">Désolé, il faut patienter une dizaine de secondes entre deux créations de documents.</div></div>'
      lockDuration = 15000
    } else {
      pressedButton.innerHTML = '<img src="/static/pics/lock.gif" alt="Veuillez patienter..." height="40" width="40">'
      tileBody.innerHTML += '<div  id="failed-creation" class="panel panel-default" style="padding: 0; margin: 0; width: 100%;"><div class="panel-body" style="background: #ffd5d5; color: #aa0000">Désolé, un problème est survenu, la feuille n\'a pas été créée. Les boutons vont redevenir disponibles dans quelques secondes. Si le problème persiste, <a href="/contact/">contactez M. Hainaux</a> !</div></div>'
      lockDuration = 15000
    }
    // console.log('[loadFile.onload]: début du timeout ' + Date.now())
    // c'est en millisecondes
    setTimeout(function () {
      pressedButton.innerHTML = '<img src="/static/pics/colored_blocks40.png" alt="Créer" height="40" width="40">'
    }, lockDuration)
    setTimeout(releaseButtons, lockDuration)
    pressedButton.classList.remove('unfaded')
  }
  request.send()
  return false
}
