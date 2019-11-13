require('sqlite3')
const sqlite3=require('sqlite3').verbose()
const db=new sqlite3.Database('./AppData/DB/share.db');

function setValue(data){
    const files=data
    return files
}
function readAll(fileType,fn){
    db.all("SELECT * FROM sharedfiles where filetype=?",[fileType],function(err,rows){
		if(err){
			console.log(err)
			console.log("Error While reading db for ")
			res.render(path.join(__dirname,'templates/db.ejs'),{error:"Error"})
        }else{
            setValue(rows)
            fn(rows)
        }
    });
}

module.exports=function (filetype,fn){
    var files;
   readAll(filetype,function(data){
       files=data;
       fn(data)
    })
}