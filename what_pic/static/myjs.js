	document.getElementById('card').style.width=document.body.clientWidth*(92/100) +"px";
    document.getElementById('card').style.height=(document.body.clientWidth*(92/100))/3.42 +"px";
    
    var get_id=document.getElementById('the_url');
    var get_id2=document.getElementById('submit_url');


    document.getElementById('upload').style.width= window.getComputedStyle(get_id).width;
    document.getElementById('upload').style.height= window.getComputedStyle(get_id).width;
    
    document.getElementById('result').style.width= window.getComputedStyle(get_id).width;
 
    var value = window.getComputedStyle(get_id2).height.replace(/[^0-9]/ig,"");
    var val2=value*2;
    document.getElementById('result').style.height= val2+"px";

    function event_happen(){
    	document.getElementById('word').style.display="none";
    	document.getElementById('add_url').style.display="none";
    	document.getElementById('arrow').style.display="none";
    	document.getElementById('upload').style.padding="0px";
        var picture=document.createElement("img");

        picture.setAttribute("max-width",window.getComputedStyle(get_id).width);
        picture.setAttribute("max-height",window.getComputedStyle(get_id).width);
        picture.setAttribute("src","");
        document.getElementById('upload').appendChild(picture);

    }
