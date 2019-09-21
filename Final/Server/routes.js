module.exports = function(app){
    app.get('/',(req,res)=>{
        res.render('index') 
    });
    app.get('/upload',(req,res)=>{
        res.render('upload')
    });
}