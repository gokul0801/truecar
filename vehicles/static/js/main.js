$(document).ready(function() {
  $("#submit").click(function() {
     $(".validate").text("");
     $("p.result").text("");            
     $("ul.result").find("li").remove();
     var vsn = $("#vsn").val();
     if (vsn.search(/^[A-Za-z]{6}[0-9]{6}$/) == -1) {
         $(".validate").text("*Please enter a valid VSN in the format of six letters (A-Z) followed by six numbers (0-9)");
     } else {
	$.post('ajax/lookupVsn/',
	       {'vsn': vsn},
	       function(data, status) {
		    if (data.empty == true) {
		      $("p.result").text("No matching records found. Please try another serial number.");
		    } else {
	              $("p.result").text("Following matching records found:");
	              $.each(data.vehicles, function(index, element) {
		        $("ul").append("<li>" + element.vehicle + "</li>");
		     });			 	
	           }
	       },
	       'json'); 
     }
   });
});
