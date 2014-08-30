window.onload = function(){
	
}

function showDiv(){
	document.getElementById("drop").style.display= "block";
	

}

$(document).mouseup(function (e)
{
    var container = $(".drop");

    if (!container.is(e.target) // if the target of the click isn't the container...
        && container.has(e.target).length === 0) // ... nor a descendant of the container
    {
        container.hide();
    }
});