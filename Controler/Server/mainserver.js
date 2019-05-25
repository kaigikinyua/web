const express=require('express');
const path=require('path');
const fs=require('fs');
const app=express();
app.set('template engine','ejs');
app.use('/video',express.static(path.join(__dirname,'Shared/videos')));
app.use('/static',express.static(path.join(__dirname,'static')));
app.use('/documents',express.static(path.join(__dirname,'Shared/documents')))
app.use('/pictures',express.static(path.join(__dirname,'Shared/pictures')))
app.get('/',function(req,res){
	var filename=fs.readFileSync('./AppData/shared.json',function(err,data){
		if(err){
			console.log('err')
		}
		return data.toString();
	});
	var files=JSON.parse(filename);
	console.log(files["videos"])
	console.log(files["documents"])
	console.log(files["pictures"])
	res.render(path.join(__dirname,'templates/index.ejs'),{videos:files["videos"],pictures:files["pictures"],documents:files["documents"]});
});
app.get('/documents/view/:filename',function(req,res){
	res.writeHead(200,{'Content-Type':'text/plain'});
	filedata=fs.createReadStream(path.join(__dirname,'Shared/documents/'+req.params.filename),'utf8');
	console.log(filedata)
	filedata.pipe(res)
});
app.listen(4000,function(){console.log("Server listening on port 4000")});