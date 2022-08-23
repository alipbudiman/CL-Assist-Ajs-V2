const thrift = require('thrift-http');
const LineService = require('LineService');

var _client = '';
var gid = '';
var kick = [];
var token = '';
var uagent = '';
var appname = '';
var appver = '';
var sysname = '';
var sysver = '';

process.argv.forEach(function (val) {
  if(val.includes('gid=')){
    gid = val.split('gid=').pop();
  }else if(val.includes('uik=')){
    kick.push(val.split('uik=').pop());
  }else if(val.includes('token=')){
    token = val.split('token=').pop();
  }else if(val.includes('uagent=')){
    uagent = val.split('uagent=').pop();
  }else if(val.includes('appname=')){
    appname = val.split('appname=').pop();
  }else if(val.includes('appver=')){
    appver = val.split('appver=').pop();
  }else if(val.includes('sysname=')){
    sysname = val.split('sysname=').pop();
  }else if(val.includes('sysver=')){
    sysver = val.split('sysver=').pop();
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
    headers: {'User-Agent':uagent,'X-Line-Application':appname+"\t"+appver+"\t"+sysname+"\t"+sysver,'X-Line-Access':token},
    path: '/S4',
    https: true
    });

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
var promise2 = func2();

Promise.all([promise2])
  .then(results => console.log(results));
