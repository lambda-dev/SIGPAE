tinymce.init({
  selector: 'textarea',
  height: 1000,
  width: 500,
  menubar: false,
  plugins: [
    'advlist autolink lists link image charmap print preview anchor',
    'searchreplace visualblocks code fullscreen',
    'table paste code'
  ],
  toolbar: 'undo redo ',
  content_css: '//www.tinymce.com/css/codepen.min.css'
});

tinymce.init({
  selector: 'textareat',
  height: 30,
  width: 500,
  menubar: false,
  plugins: [
    'advlist autolink lists link image charmap print preview anchor',
    'searchreplace visualblocks code fullscreen',
    'table paste code'
  ],
  toolbar: 'undo redo ',
  content_css: '//www.tinymce.com/css/codepen.min.css'
});