CKEDITOR.plugins.add('ImageSelector', {
    icons: 'ImageSelector',
    init: function(editor) {
      editor.addCommand('ImageSelectorDialog', new CKEDITOR.dialogCommand('ImageSelectorDialog'));
  
      editor.ui.addButton('ImageSelector', {
        label: 'Select Image',
        command: 'ImageSelectorDialog',
        toolbar: 'insert',
      });
  
      CKEDITOR.dialog.add('ImageSelectorDialog', function() {
        return {
          title: 'Insert Image',
          minWidth: 400,
          minHeight: 200,
          contents: [
            {
              id: 'tab-basic',
              label: 'Basic Settings',
              elements: [
                {
                  type: 'file',
                  id: 'image',
                  label: 'Image',
                  validate: CKEDITOR.dialog.validate.notEmpty('Please select an image file.'),
                  onChange: function() {
                    var dialog = this.getDialog();
                    var fileLoader = dialog.getContentElement('tab-basic', 'fileLoader');
                    fileLoader.loadAndPreviewImage(this.getValue());
                  },
                },
                {
                  type: 'html',
                  id: 'preview',
                  label: 'Preview',
                  style: 'width: 100%; height: 150px; text-align: center',
                  html: '<img id="previewImage" src="" style="max-width: 100%; max-height: 100%">',
                },
                {
                  type: 'fileLoader',
                  id: 'fileLoader',
                  label: 'Preview',
                  onLoad: function(event) {
                    var dialog = this.getDialog();
                    var preview = dialog.getContentElement('tab-basic', 'preview');
                    preview.getElement().getChild(0).setAttribute('src', event.data);
                  },
                },
              ],
            },
          ],
          onOk: function() {
            var dialog = this;
            var fileLoader = dialog.getContentElement('tab-basic', 'fileLoader');
            var file = fileLoader.file;
            if (file) {
              var reader = new FileReader();
              reader.onload = function(event) {
                var data = event.target.result;
                var imgElement = '<img src="' + data + '">';
                editor.insertHtml(imgElement);
              };
              reader.readAsDataURL(file);
            }
          },
        };
      });
    },
  });
  