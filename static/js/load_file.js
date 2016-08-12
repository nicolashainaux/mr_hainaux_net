window.addEventListener('load', registerEvents, false)

function registerEvents (event) {
  var mmButtons = document.querySelectorAll('.btn-mm')
  for (var i = 0; i < mmButtons.length; ++i) {
    mmButtons[i].addEventListener('click', loadFile, false)
  }
}

function loadFile (event) {
  event.preventDefault()
  // console.log('[loadFile]: this.getAttribute("href") = ' + this.getAttribute('href'))
  // console.log('[loadFile]: event.target = ' + event.target)
  var request = new XMLHttpRequest()
  var url = this.getAttribute('href')
  // Create a link object that will be used in fact to parse the url
  // in order to get the file name
  var parser = document.createElement('a')
  parser.href = this.getAttribute('href')
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
      // useless and not working:
      // remove `a` following `Save As` dialog,
      // once `window` regains `focus`
      // window.onfocus = function () {
      //   document.body.removeChild(a)
      // }
    }
  }
  request.send()
  return false
}
