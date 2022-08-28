const thrift = require('thrift-http');
const LineService = require('LineService');
const jsonData = require('./statusalip.json'); 

var _client = '';
var gid = '';
var kick = [];
var token = '';
var mod = '';

process.argv.forEach(function (val) {
  if(val.includes('gid=')){
    gid = val.split('gid=').pop();
  }else if(val.includes('uik=')){
    kick.push(val.split('uik=').pop());
  }else if(val.includes('token=')){
    token = val.split('token=').pop();
  }else if(val.includes('mod=')){
    mod = val.split('mod=').pop();
  }
});

function setTHttpClient(options) {
    var connection =
      thrift.createHttpConnection('gw.line.naver.jp', 443, options);
    connection.on('error', (err) => {
      console.log('err',err);
      return err;
    });
    _client = thrift.createHttpClient(LineService, connection);
  }

setTHttpClient(options={
    protocol: thrift.TCompactProtocol,
    transport: thrift.TBufferedTransport,
    headers: {'User-Agent':jsonData["headersAjs"],'X-Line-Application':jsonData["headersAssist"],'X-Line-Access':token},
    path: '/S4',
    https: true
    });

async function func1() {

  let promise1 = new Promise((resolve, reject) => {
    try {
    for (var i=0; i < cancel.length; i++) {
      _client.cancelGroupInvitation(0, gid, [cancel[i]]);
    }
    resolve("Cancel Done")
    } catch(e) {
    reject(e);
    }
  });
  return promise1;
}

async function func2() {

  let promise2 = new Promise((resolve, reject) => {
    try {
    for (var i=0; i < kick.length; i++) {
      _client.kickoutFromGroup(0, gid, [kick[i]]);
    }
    resolve("Kick Done")
    } catch(e) {
    reject(e);
    }
  });
  return promise2;
}
var promise1 = func1();
var promise2 = func2();

function RunPromise(){
  if (mod == "single") {
    Promise.all([promise2])
    .then(results => console.log(results));
  } else {
    Promise.all([promise2,promise1])
    .then(results => console.log(results));
  }
}

RunPromise()
