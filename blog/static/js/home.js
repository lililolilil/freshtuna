var mySite = function(){

}
var mySite_home = function(){
	mySite.call(this); 

	var now = null; 
	
	var $article = $(".home_article"); 

	this.init = function(){
		displayArticle(); 
		addEvent(); 
	}

	var displayArticle = function(){
		var container = $("<div></div>"), 
			con_idx= $article.length/3, 
			num = con_idx+1;
		for(var i = 0 ; i <num ; i++){
			container.append("<div class='art_con'></div>"); 
		} 

		var $art_con = $(".art_con", container); 
		$article.each(function(idx){
			art_num = parseInt(idx/3); 
			$art_con.eq(art_num).append($(this).attr("data-index",idx)); 
		}); 
		$(".home_container").html(container.html()); 
	}

	var addEvent = function(){
		$article = $(".home_article"); 
		var $art_con = $(".art_con");

		$article.on("mouseover", function(e){

			 e.stopPropagation();
	        var $this = $(this), 
	        	index = $(this).data("index"); 
	        	$mybro = $this.parent().find(".home_article"); 
			if(now != index){
				$(".in").removeClass("in col-sm-6").addClass("col-sm-4"); 
				$(".out").removeClass("out col-sm-3").addClass("col-sm-4"); 
	        	$mybro.not($this).removeClass("col-sm-6 in").addClass("col-sm-3 out");
	        	$this.removeClass("col-sm-3 col-sm-4 out").addClass("col-sm-6 in"); 	
	        	now = index; 
	        }

		});  
	}
	    /*$(document).on("click", ".home_article", function(e){
		var $this = $(this); 
		var data = $this.data(); 
		var url = contextPath+"/board/view", query = "?returnUrl="+location.href; 
		$.each(data, function(key,value){
		    query += "&"+key+"="+value; 
		})
		location.href=url+query; 
	    }); 
	}*/
}
