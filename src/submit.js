$(function () {
                $(":file").change(function () {
                    if (this.files && this.files[0]) {
                        var reader = new FileReader();
        
                        reader.onload = imageIsLoaded;
                        reader.readAsDataURL(this.files[0]);
                    }
                });
            });
        
            function imageIsLoaded(e) {
                $('#myImg').attr('src', e.target.result);
                $('#yourImage').attr('src', e.target.result);
            };
            function previewFile(){
               var preview = document.querySelector('img'); //selects the query named img
               var file    = document.querySelector('input[type=file]').files[0]; //sames as here
               var reader  = new FileReader();
        
               reader.onloadend = function () {
                   preview.src = reader.result;
               }
        
               if (file) {
                   reader.readAsDataURL(file); //reads the data as a URL
               } else {
                   preview.src = "";
               }
          }

          previewFile(); 