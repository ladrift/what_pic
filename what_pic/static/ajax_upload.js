function file_upload() {
    $('#upload_btn').click(function() {
        console.log('upload click');
        event.preventDefault();
        var form_data = new FormData($('#uploadform')[0]);
        // disable the input button
        $('input#submit_url').prop('disabled', true);
        $('input#image').prop('disabled', true);
        $('#show_result').text('processing...');
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            processData: false,
            dataType: 'json'
        }).done(function(data, textStatus, jqXHR){
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
            console.log('Success!');
            // enable the button
            $('input#submit_url').prop('disabled', false);
            $('input#image').prop('disabled', false);
            if (data['type'] == 'result') {
                $("#show_result").text(data['content']);
            } else if (data['type'] == 'mistake') {
                $("#show_result").text('Mistake happened');
            }
        }).fail(function(data){
            alert('error!');
        });
    });
}

function previewImage(file) {
    // preview the image using base64 data URI
    var imageType = /^image\//;

    if (!imageType.test(file.type)) {
        console.log('not image')
        return;
    }

    console.log('is image');
    // remove previous
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
    picture.setAttribute("src","");
    document.getElementById('upload').appendChild(picture);

    $('#img_thumbnail')[0].file = file;

    var reader = new FileReader();
    reader.onload = (function(aImg) { return function(e) { aImg.src = e.target.result; }; })($('#img_thumbnail')[0]);
    reader.readAsDataURL(file);
}

function handle_files(files) {
    document.getElementById('word').style.display="none";
    document.getElementById('add_url').style.display="none";
    document.getElementById('arrow').style.display="none";
    document.getElementById('upload').style.padding="0px";

    previewImage(files[0]);

    // trigger submit button to upload the file
    upload_btn = document.getElementById('upload_btn');
    upload_btn.click();
}
    
function debug_upload_file(e) {
    console.log(e);
}
