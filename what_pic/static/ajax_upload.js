function file_upload() {
    $('#upload').click(function() {
        console.log('upload click')
        event.preventDefault();
        var form_data = new FormData($('#uploadform')[0]);
        $('#result').text('processing...')
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
            if (data['type'] == 'result') {
                $("#result").text(data['content']);
            } else if (data['type'] == 'mistake') {
                $("#result").text('Mistake happened');
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

    console.log('is image')
    $('#img_thumbnail')[0].file = file;

    var reader = new FileReader();
    reader.onload = (function(aImg) { return function(e) { aImg.src = e.target.result; }; })($('#img_thumbnail')[0]);
    reader.readAsDataURL(file);
}

function handle_files(files) {
    // trigger submit button

    previewImage(files[0])
}
    

