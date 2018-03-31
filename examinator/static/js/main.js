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
                let report = document.getElementById("report");
                report.innerHTML = response.result;
            },
            error: function(result) {
                console.log(result)
            }
        })
    }
}
