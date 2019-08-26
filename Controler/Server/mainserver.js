const express=require('express');
const path=require('path');
const fs=require('fs');
const app=express();

const sqlite3=require('sqlite3').verbose();
const db=new sqlite3.Database(path.join(__dirname,'../AppData/share.db'));
app.set('template engine','ejs');
app.use('/video',express.static(path.join(__dirname,'Shared/videos')));
app.use('/static',express.static(path.join(__dirname,'static')));
app.use('/documents',express.static(path.join(__dirname,'Shared/documents')))
app.use('/pictures',express.static(path.join(__dirname,'Shared/pictures')))
app.use('/others',express.static(path.join(__dirname,'Shared/others')))
app.use('/db',express.static('/'))
app.get('/',function(req,res){
	var filename=fs.readFileSync('./AppData/shared.json',function(err,data){
		if(err){
			console.log('err')
		}
		return data.toString();
	});
	var files=JSON.parse(filename);
	res.render(path.join(__dirname,'templates/index.ejs'),{videos:files["videos"],pictures:files["pictures"],documents:files["documents"],others:files["others"]});
});
app.get('/documents/view/:filename',function(req,res){
	res.writeHead(200,{'Content-Type':'text/plain'});
	filedata=fs.createReadStream(path.join(__dirname,'Shared/documents/'+req.params.filename),'utf8');
	filedata.pipe(res)
});

app.get('/database',function(req,res){
	var files=db.all("SELECT * FROM sharedfiles",[],function(err,rows){
		if(err){
			console.log(err)
			res.render(path.join(__dirname,'templates/db.ejs'),{error:"Error"})
		}
		rows.forEach(row => {
			console.log(row.path)
		});
		res.render(path.join(__dirname,'templates/db.ejs'),{paths:rows})
	});
});

app.listen(4000,function(){console.log("Server listening on port 4000")});