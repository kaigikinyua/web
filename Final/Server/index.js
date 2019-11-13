const express=require('express')
const app=express()

const routes=require('./routes.js')
app.set('view engine','ejs');
app.use('/static',express.static('./static'))
app.use('/media',express.static('/'))

app.listen(4000,()=>{ console.log("Server Running on port 4000")})
routes(app);