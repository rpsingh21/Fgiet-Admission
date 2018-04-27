var MAX_SIZE = 200*1024
var ugOrDiplompassing = ['id_ugOrDiplompassingYear','id_ugOrDiplomBoard','id_ugOrDiplomBranch','id_ugOrDiplomPercentageMarks','id_ugOrDiplomResultimage']
var intermediatePassing =['id_intermediatePassingYear','id_intermediateBoard','id_intermediatePercentageMarks','id_intermediateResultImage']

function ValidateFileUpload(ele_id) {
    var fuData = document.getElementById(ele_id);
    var FileUploadPath = fuData.value;
    if (FileUploadPath == '') {
        alert("Please upload an image");
    }
    else {
        var Extension = FileUploadPath.substring(FileUploadPath.lastIndexOf('.') + 1).toLowerCase();
        if (Extension == "gif" || Extension == "png"|| Extension == "jpeg" || Extension == "jpg") {
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
            alert("Photo only allows file types of GIF, PNG, JPG, JPEG");
            fuData.value = "";
        }
    }
}

function changeRequirment(){
    var year = document.getElementById("id_applyYear").value;
    var course = document.getElementById("id_course").value;
    if(year == "1" && course == "MCA"){
        for(var id in ugOrDiplompassing){
            document.getElementById(ugOrDiplompassing[id]).required = true;
        }
        for(var id in intermediatePassing){
            document.getElementById(intermediatePassing[id]).required = true;
        }
    }
    else if(year == 2 && course == "BTech"){
        for(var id in ugOrDiplompassing){
            document.getElementById(ugOrDiplompassing[id]).required = true;
        }
        for(var id in intermediatePassing){
            document.getElementById(intermediatePassing[id]).required = false;
        }
    }
    else if(year == 1 && course == "BTech"){
        for(var id in ugOrDiplompassing){
            document.getElementById(ugOrDiplompassing[id]).required = false;
        }
        for(var id in intermediatePassing){
            document.getElementById(intermediatePassing[id]).required = true;
        }
    }
    else{
        for(var id in ugOrDiplompassing){
            document.getElementById(ugOrDiplompassing[id]).required = true;
        }
        for(var id in intermediatePassing){
            document.getElementById(intermediatePassing[id]).required = true;
        }
    }
}

$("document").ready(function(){
    $("input[type=file]").change(function(){
        ValidateFileUpload(this.id);
    });
    
    $("#id_applyYear").change(function(){
        if(document.getElementById("id_course").value){
            changeRequirment();
        }
    });

    $("#id_course").change(function(){
        if(document.getElementById("id_applyYear").value){
            changeRequirment();
        }
    })
});


