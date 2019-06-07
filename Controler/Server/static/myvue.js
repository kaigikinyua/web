var nav=new Vue({
	el:'#topBarner',
	data:{
		documents:false,
		videos:true,
		image:false,
		others:false
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
		},
	}
});
var documents=new Vue({
	el:'#documents',
	data:{},
	methods:{
		documents:function(){
			return nav.documents
		}
	}
})
var image=new Vue({
	el:'#pictures',
	data:{},
	methods:{
		image:function(){
			return nav.image
		}
	}
})
var others=new Vue({
	el:'#others',
	data:{},
	methods:{
		others:function(){
			return nav.others
		}
	}
})
