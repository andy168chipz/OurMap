//http://newsignature.github.io/us-map/

var cur_page;
var statename;
$(document).ready(function() {
		 $('#map').usmap({

		 stateHoverAnimation: 200,


		//click function
		click: function(event, data) {
			$('#links').css('display', 'none');
			 statename = data.name;
			$loading = $('#loading');
			$link = $('#links');
			ajaxCall(statename,cur_page);

		}
	});
    //for dynamic content
	$("#pages").on('click', 'button',function() {
         if(this.value != cur_page){
            ajaxCall(statename,this.value);
         }

    });

});

function ajaxCall(state, page){
    page = page == null ? 1: page;
    $.ajax({
				url:"/image",
				type:'POST',
				data: { 'state':state,'cur_page':page},
				dataType: "json",
				cache:true,
				beforeSend: function() {
				    init();
    				$loading.html("<img src='/img/loading.gif' />");
  				},
				success: function(data){
				    //success with no pics
					$loading.html("");
					if(data.url_dict ==""){
                        haveNotBeen();
					}
					else{
					//success with pics
					    cur_page=data.page;
					    console.log('cur_page='+cur_page);
                        pages(data.pages_count);
                        links(data.url_dict);
                        window.location="#links";
                    }
				},
				error: function(html){
				    $loading.hide();
				    $('#error').show();
					console.log('fail');
				}
			});
}


function pages(pages){
    var buttons = "";
    for(i =1; i <= pages; i++){
            buttons += '<button id=page'+i+' type="button" class="btn btn-info " role="button" value='+i+'>'+i+'</button>';
    }
    $('#pages').html("");
    $('#pages').append(buttons);
    $('#pages').show();
}

function links(url_dict){
    $link = $('#links');
    $link.html("");
    $link.append(url_dict);
    $link.show();
}

function init(){
    $link.html("");
    $('#pages').html("");
    $link.hide();
    $('#pages').hide();
}
function haveNotBeen(){
    $link.html("");
    $('#pages').html("");
    $('#pages').html('<div class="bg-warning" >'+"Looks like we haven't been there :("+'</div>');
    $('#pages').show();
}