var MAX_SIZE = 500*1024
var ugOrDiplompassing = ['id_ugOrDiplompassingYear','id_ugOrDiplomBoard','id_ugOrDiplomBranch','id_ugOrDiplomPercentageMarks','id_ugOrDiplomResultimage']
var intermediatePassing =['id_intermediatePassingYear','id_intermediateBoard','id_intermediatePercentageMarks','id_intermediateResultImage']
var mcaFields = ['id_math','id_physics','id_chemistry']

function ValidateFileUpload(ele_id) {
    var fuData = document.getElementById(ele_id);
    var FileUploadPath = fuData.value;
    if (FileUploadPath == '') {
        alert("Please upload an image");
    }
    else {
        var Extension = FileUploadPath.substring(FileUploadPath.lastIndexOf('.') + 1).toLowerCase();
        if (Extension == "png"|| Extension == "jpeg" || Extension == "jpg") {
            if (fuData.files && fuData.files[0]) {
                var size = fuData.files[0].size;
                console.log(size);
                if(size > MAX_SIZE){
                    alert("Maximum file size exceeds");
                    fuData.value = "";
                    return;
                }
                else{
                    var reader = new FileReader();
                    reader.onload = function(e) {
                        $('#blah').attr('src', e.target.result);
                    }
                    reader.readAsDataURL(fuData.files[0]);
                }
            }
        } 
    else {
            alert("Photo only allows file types of PNG, JPG, JPEG");
            fuData.value = "";
        }
    }
}

$("document").ready(function(){
    $("input[type=file]").change(function(){
        ValidateFileUpload(this.id);
    });
    $("#id_applyYear").val(year);
    $("#id_course").val(course);
    $("#id_applyYear").parent().parent().hide();
    $("#id_course").parent().parent().hide();

    $("input[type=select").addClass('custom-select');

    $("#form_submit").click(function(){
        console.log("click");
        $('#form_model').modal('show');
    });
});
