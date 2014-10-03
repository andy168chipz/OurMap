//http://newsignature.github.io/us-map/

$(document).ready(function() {
		 $('#map').usmap({

		 stateHoverAnimation: 200,


		//click function
		click: function(event, data) {
			$('#links').css('display', 'none');
			 var statename = data.name;
			 console.log(statename);
			 //http://stackoverflow.com/questions/9509191/google-app-engine-with-ajax-request-and-python-interactions
			$.ajax({
				url:"/image",
				type:'GET',
				success: function(html){

					$('#links').show();
				},
				error: function(html){
					console.log('fail');
				}
			});
		}
		 });

});