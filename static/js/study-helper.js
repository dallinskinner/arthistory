$(document).ready(function(){
	$('.image').click(function(){
		$(this).siblings('.info').toggle('fast');
	})

	$('.sort-heading').click(function(){
		$(this).next('.description').toggle('fast');
	})
});