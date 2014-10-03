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
				type:'POST',
				data: { 'state':data.name},
				beforeSend: function() {
    				$('#loading').html("<img src='/img/loading.gif' />");
  				},
				success: function(html){
					//$('#loading').html("");
					console.log(html);
					$link = $('#links');
					$link.show();

				},
				error: function(html){
					console.log('fail');
				}
			});
		}
		 });

});