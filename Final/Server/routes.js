const db=require('./db.js')
const fs=require('fs')
const bodyParser=require('body-parser')
var urlencodedParser=bodyParser.urlencoded({extended:false})
module.exports = function(app){
    app.get('/',(req,res)=>{
        res.render('index') 
    });
    app.get('/videos',(req,res)=>{
        db('videos',function(videos){
            res.render('videos',{videos:videos})
        });
    });
    app.get('/audio',(req,res)=>{
        db('audio',audio=>{
            res.render('audio',{audio:audio})
        })
    });
    app.get('/documents',(req,res)=>{
        db('documents',documents=>{
            res.render('documents',{documents:documents})
        })
    })
    app.get('/text',(req,res)=>{
        db('text',text=>{
            res.render('text',{text:text})
        })
    });
    app.get('/pictures',(req,res)=>{
        db('pictures',pictures=>{
            res.render('pictures',{pictures:pictures})
        })
    });
    app.get('/compressed',(req,res)=>{
        db('compressed',compressed=>{
            res.render('compressed',{comp:compressed})
        })
    })

    app.post('/readFile',urlencodedParser,(req,res)=>{

        filepath=req.body.filepath
        res.writeHead(200,{'Content-Type':'text/plain'});
	    filedata=fs.createReadStream(filepath,'utf8');
        filedata.pipe(res)
    })
    app.post('/readPdf',urlencodedParser,(req,res)=>{
        filepath=req.body.filepath
        res.sendFile(filepath)
    })
    app.get('/getAllFileData',(req,res)=>{
        var myjson={
            "Videos":[{"name":"Video One"},{"name":"Video Two"}],
            "Documents":[{"name":"Doc One"},{"name":"Doc Two"}]
        }
        res.end(JSON.stringify(myjson))
    });
}