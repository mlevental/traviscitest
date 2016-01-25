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

function longProcess() {
    var $divForProgressBar = $(emptydiv);

    // Wenn nicht vorhanden dann Progressbar hinzufügen
    if (!$divForProgressBar.find('.progress-bar').length) {
        $divForProgressBar.append(
            '<div class="progress">' +
            '<div class="progress-bar progress-bar-info progress-bar-striped active" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="min-width: 2em;">' +
            '0% ' +
            '</div>' +
            '</div>'
        );
    }

    // Request senden und periodisch erneut anfragen
    var $progressBar = $('#emptydiv .progress-bar');
    startAndUpdateProgress($progressBar, true);
}

function startAndUpdateProgress($progressBar, initialRequest) {
    var url = initialRequest ? 'longprocess' : 'updatelongprocess';

    $.ajax({
        type: "POST",
        url: url,
        data: {csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
        datatype: "JSON",
        success: function (data) {
            var processCompleted = data['processCompleted'];

            if (processCompleted) {
                $progressBar.text('100%');
                $progressBar.width('100%');
            }
            else {
                var progress = data['progress'];

                // wieder Request absenden um Fortschritt zu aktualisieren
                if (progress >= 0 && progress < 100) {
                    $progressBar.text(progress + '%');
                    $progressBar.width(progress + '%');

                    setTimeout(function () {
                        startAndUpdateProgress($progressBar, false)
                    }, 1000);
                }
            }
        },
        failure: function (data) {
            alert('Error!');
        }
    });
}