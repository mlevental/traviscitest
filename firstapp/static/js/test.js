function sendemail() {
    $.ajax({
        type: "POST",
        url: 'sendemail',
        data: {csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
        datatype: "JSON",
        success: function (data) {
            alert('Success, data: ' + data['testKey'])
        },
        failure: function (data) {
            alert('Error, data: ' + data);
        }
    });
}

