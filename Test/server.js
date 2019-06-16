const path=require('path')
const express=require('express')
const app=express()
app.use('/vol1',express.static('/run/media/antony/New Volume'))
app.get('/',(req,res)=>{
    res.sendFile(path.join(__dirname,'index.html'))
});
app.listen(4000,()=>{console.log('Server Running on port: 4000')})