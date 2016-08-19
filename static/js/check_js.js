window.addEventListener('load', unhideWrapper, false)

function unhideWrapper (event) {
  document.querySelector('#no-js').style.display = 'none'
  document.querySelector('.wrapper').style.display = 'block'
  displayDeprecatedBrowserWarning()
}

function displayDeprecatedBrowserWarning () {
  if (typeof Promise !== 'undefined' &&
      Promise.toString().indexOf('[native code]') !== -1) {
    var a = document.createElement('a')
    if (typeof a.download !== 'undefined') {
      document.querySelector('#deprecated-browser-warning').style.display = 'none'
    }
  }
}
