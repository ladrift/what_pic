function url_submit() {
    $('#submit_url').click(function() {
        // disable the button
        $('input#submit_url').prop('disabled', true)
        $('input#image').prop('disabled', true)
        event.preventDefault();
        
        // clean words
        document.getElementById('word').style.display="none";
        document.getElementById('add_url').style.display="none";
        document.getElementById('arrow').style.display="none";
        document.getElementById('upload').style.padding="0px";

        // remove previous image if exists
        if (document.contains(document.getElementById('img_thumbnail'))) {
            document.getElementById('img_thumbnail').remove();
        }
        // add image
        var picture=document.createElement("img");
        var max_width = window.getComputedStyle(get_id).width;
        var max_height = window.getComputedStyle(get_id).width;
        var num_mwidth = max_width.replace(/[^0-9]/ig, "") * 0.9;
        var num_mheight = max_height.replace(/[^0-9]/ig, "") * 0.9;
        picture.setAttribute("style","max-height:"+num_mheight+"px; max-width:"+num_mwidth+"px;");
        picture.setAttribute("id","img_thumbnail");
        picture.setAttribute("src", $('input#the_url').val());

        document.getElementById('upload').appendChild(picture);

        $('#show_result').text('processing...');
        if ($('input#the_url').val() != '') {
            $.getJSON($SCRIPT_ROOT + '/_url_submit', {
                type: 'url',
                content: $('input#the_url').val()
            }, function(data) {
                console.log(data);
                // enable the button
                $('input#submit_url').prop('disabled', false);
                $('input#image').prop('disabled', false);
                // clean the input text
                $('input#the_url').val('');
                if (data.type == 'mistake') {
                    $('#show_result').text('mistake happened');
                } else if (data.type == 'result') {
                    $('#show_result').text(data.content);
                }
            });
        }
        return false;
    });
}
