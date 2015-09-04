function url_submit() {
    $('#submit_url').click(function() {
        event.preventDefault();
        
        if ($('input#the_url').val() != '') {
            // disable the button

            $('button#submit_url').prop('disabled', true)
            $('input#image').prop('disabled', true)
            // clean words
            document.getElementById('panel-text').style.display="none";

            // remove previous image if exists
            if (document.contains(document.getElementById('img_thumbnail'))) {
                document.getElementById('img_thumbnail').remove();
            }
            // add image
            var get_id=document.getElementById('the_url');
            var get_id2=document.getElementById('submit_url');
            var picture=document.createElement("img");
            var max_width = window.getComputedStyle(get_id).width;
            var max_height = window.getComputedStyle(get_id).width;
            var num_mwidth = max_width.replace(/[^0-9]/ig, "") * 0.9;
            var num_mheight = max_height.replace(/[^0-9]/ig, "") * 0.9;
            picture.setAttribute("style","max-height: 270px; max-width:"+num_mwidth+"px;");
            picture.setAttribute("id","img_thumbnail");
            picture.setAttribute("src", $('input#the_url').val());
            picture.setAttribute("class","img-responsive center-block");

            document.getElementById('upload').appendChild(picture);

            $('#show_result').text('processing...');
            $.getJSON($SCRIPT_ROOT + '/_url_submit', {
                type: 'url',
                content: $('input#the_url').val()
            }, function(data) {
                console.log(data);
                    // enable the button
                    $('button#submit_url').prop('disabled', false);
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
