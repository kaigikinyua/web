function fetchdata(url,fn){ 
    fetch(url)
    .then(res=> res.json())
    .then(myjson=>fn(myjson))
}

function getAllFileData(){
    url="http://localhost:4000/getAllFileData"
    fetchdata(url,(data)=>{
        search(data)
    })
}

function search(){
    
}