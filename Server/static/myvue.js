var nav=new Vue({
	el:'#topBarner',
	data:{
		documents:false,
		videos:false,
		image:false
	},
	methods:{},
	computed:{}
});
var module=new Vue({
	el:'#video',
	data:{},
	methods:{
		documents:function(){
			console.log("documents")
			return nav.documents
		},
		video:function(){
			console.log("videos")
			return nav.videos
		},
		image:function(){
			console.log("image")
			return nav.image
		}
	},
	computed:{}
});