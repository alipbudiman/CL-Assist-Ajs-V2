const thrift = require('thrift-http');
const LineService = require('LineService');

var _client = '';
var gid = '';
var kick = [];
var token = ''; 

process.argv.forEach(function (val) {
  if(val.includes('gid=')){
    gid = val.split('gid=').pop();
  }else if(val.includes('uik=')){
    kick.push(val.split('uik=').pop());
  }else if(val.includes('token=')){
    token = val.split('token=').pop();
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
    headers: {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36','X-Line-Application':'CHROMEOS\t2.4.9\tChrome OS\t1','X-Line-Access':token},
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
