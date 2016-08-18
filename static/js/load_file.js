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
}

function loadFile (event) {
  event.preventDefault()
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
  // Create a link object that will be used in fact to parse the url
  // in order to get the file name
  var parser = document.createElement('a')
  parser.href = url
  // var sheetName = parser.pathname.split('/')[2]
  var pdfFileName = parser.pathname.split('/')[3]
  // console.log('[loadFile]: sheetName / pdfFileName = ' + sheetName + ' / ' + pdfFileName)
  request.open('GET', url, true)
  request.responseType = 'blob'
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
    }
    // console.log('[loadFile.onload]: début du timeout ' + Date.now())
    // c'est en millisecondes
    setTimeout(releaseButtons, 10000)
    setTimeout(function () {
      pressedButton.innerHTML = '<img src="/static/pics/colored_blocks40.png" alt="Créer" height="40" width="40">'
    }, 10000)
    pressedButton.classList.remove('unfaded')
  }
  request.send()
  return false
}
