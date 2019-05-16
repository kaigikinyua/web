const express=require('express');
const path=require('path');
const fs=require('fs');
const app=express();
app.set('template engine','ejs');
app.use('/video',express.static('/home/antony/Videos'));
app.use('/static',express.static(path.join(__dirname,'static')));
app.get('/',function(req,res){
	var filename=fs.readFileSync('./AppData/shared.json',function(err,data){
		if(err){
			console.log('err')
		}
		return data.toString();
	});
	var files=JSON.parse(filename);
	console.log(files["videos"])
	res.render(path.join(__dirname,'templates/index.ejs'),{videos:files["videos"]});
});
app.listen(4000,function(){console.log("Server listening on port 4000")});