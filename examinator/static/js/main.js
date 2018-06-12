function generate()
{
    var answer = document.getElementById("answer-area").value;
    var blueprint = document.getElementById("blueprint-area").value;
    if(answer === '' || blueprint === ''){
        alert("Please enter the answer and blueprint!!!")
    }
    else {
        $.ajax({
            type: "POST",
            dataType: "json",
            url: '/generate/',
            data:{
                'answer':answer,
                'blueprint':blueprint,
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                console.log(response.result)
                let report = document.getElementById("result");
                report.innerHTML = response.result;
            },
            error: function(result) {
                console.log(result)
            }
        })
    }
}

function download_answer()
{
    var answer = document.getElementById("answer-area").value;
    if(answer === ''){
        alert("Please enter the answer!!!")
    }
}

function download_blueprint()
{
    var blueprint = document.getElementById("blueprint-area").value;
    if(blueprint === ''){
        alert("Please enter the blueprint!!!")
    }
}
