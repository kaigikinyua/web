const db=require('./db.js')
const fs=require('fs')
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

    app.get('/readFile',(req,res)=>{
        filepath=req.query
        res.writeHead(200,{'Content-Type':'text/plain'});
	    filedata=fs.createReadStream(filepath,'utf8');
        filedata.pipe(res)
    })
    app.get('/upload',(req,res)=>{
        res.render('upload')
    });
}