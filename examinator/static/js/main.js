function generate(){
    var answer = document.getElementById("answer-area").value;
    var blueprint = document.getElementById("blueprint-area").value;
    if(answer === '' || blueprint === ''){
        alert("Please enter the answer and blueprint!!!")
    }
}

function download_answer()
{
    var answer = document.getElementById("answer-area").value;
    if(answer === ''){
        alert("Please enter the answer!!!")
    }
    else {
        var filename = "answersheet"+new Date().getTime()+".txt";
        download(filename, answer);
    }
}

function download_blueprint()
{
    var blueprint = document.getElementById("blueprint-area").value;
    if(blueprint === ''){
        alert("Please enter the blueprint!!!")
    }
    else {
        var filename = "blueprint"+new Date().getTime()+".txt";
        download(filename, blueprint);
    }
}

function download(filename, downloadable){
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(downloadable));
    element.setAttribute('download',filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}