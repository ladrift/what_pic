function show_pic() {
    var ar=document.getElementById('url');
    var urll=ar.value;
    document.getElementById('img_thumbnail').src=urll;
    document.getElementById('result').innerHTML = 'uploading...'

    sendURL(urll)
}
