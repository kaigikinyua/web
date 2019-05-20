var nav=new Vue({
	el:'#topBarner',
	data:{
		documents:false,
		videos:false,
		image:false
	},
	methods:{}
});
var video=new Vue({
	el:'#video',
	data:{},
	methods:{
		video:function(){
			console.log("videos")
			return nav.videos
		}
	}
});
var documents=new Vue({
	el:'#documents',
	data:{},
	methods:{
		documents:function(){
			console.log("documents")
			return nav.documents
		}
	}
})
var image=new Vue({
	el:'#pictures',
	data:{},
	methods:{
		image:function(){
			console.log("image")
			return nav.image
		}
	}
})
