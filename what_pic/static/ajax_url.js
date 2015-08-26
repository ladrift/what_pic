function url_submit() {
    $('#submit').click(function() {
        event.preventDefault();
        $('#img_thumbnail')[0].src = $('input#url').val();
        $('#result').text('processing...');
        if ($('input#url').val() != '') {
            $.getJSON($SCRIPT_ROOT + '/_url_submit', {
                type: 'url',
                content: $('input#url').val()
            }, function(data) {
                console.log(data);
                if (data.type == 'mistake') {
                    $('#result').text('mistake happened');
                } else if (data.type == 'result') {
                    $('#result').text(data.content);
                }
            });
        }
        return false;
    });
}
