var jsonfile = require('jsonfile')
var fs = require('fs');

function save() {

  var file = 'settings.json'
  var tcks = document.getElementById('tck').value
  var ask = document.getElementById('ack').value
  var dbc = document.getElementById('dbc').value
  var sk = document.getElementById('sk').value
  var surl = document.getElementById('surl').value
  var tcks = tcks.replace(" ", "")
  var ask = ask.replace(" ", "")
  var dbc = dbc.replace(" ", "")

  var obj = {
    "sitekey": sk,
    "url": surl,
    "tcks": tcks,
    "acks": ask,
    "dbks": dbc
  }
  jsonfile.writeFile(file, obj, {spaces: 2}, function(err) {
    console.error(err)
  })
  signale.success("Saved Configuration")
  document.getElementById('statusI').innerHTML = "Saved Config!"
  return false
}
