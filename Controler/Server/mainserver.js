const express=require('express');
const path=require('path');
const fs=require('fs');
const app=express();

const sqlite3=require('sqlite3').verbose();
const db=new sqlite3.Database(__dirname+'/share.db',(err)=>{if (err){console.log("Error Connecting to "+__dirname+"share.db")}else{ console.log("Connecting ")}});
app.set('template engine','ejs');
app.use('/static',express.static(path.join(__dirname,'static')));
app.use('/db',express.static('/'))

//index
app.get('/',function(req,res){
	var files_v=db.all("SELECT * FROM sharedfiles where filetype=?",['videos'],function(err,rows){
		if(err){
			console.log(err)
			console.log("Error While reading db for ")
			res.render(path.join(__dirname,'templates/db.ejs'),{error:"Error"})
		}
		else{
			var videos=rows
			var files_p=db.all("SELECT * FROM sharedfiles where filetype=?",['pictures'],function(err,rows){
				if(err){
					console.log(err)
					console.log("Error while reading db for pictures")
				}
				else{
					var pictures=rows
					var files_d=db.all("SELECT * FROM sharedfiles where filetype=?",['documents'],function(err,rows){
						if(err){
							console.log(err)
							console.log("Error while reading db for documents")
						}
						else{
							var documents=rows
							console.log(videos)
							console.log(pictures)
							console.log(documents)
							res.render(path.join(__dirname,'templates/db.ejs'),{videos:videos,pictures:pictures,documents:documents})
						}
					});
				}
			});
		}
	});
});

//text documents
app.get('/documents/view/:filename',function(req,res){
	res.writeHead(200,{'Content-Type':'text/plain'});
	filedata=fs.createReadStream(path.join(__dirname,'Shared/documents/'+req.params.filename),'utf8');
	filedata.pipe(res)
});

//test
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