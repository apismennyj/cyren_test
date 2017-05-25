$(document).ready(function () {

    $.ajaxSetup({
        beforeSend: function (xhr, options) {
            xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'))
        }
    })

    $('#user_status_form').on('change', function (e) {
        $.ajax({
            type: 'POST',
            data: $(this).serialize(),
            url: $(this).attr('action'),
            success: function (result) {
                if (200 == result['status_code']) {
                    reload_controlcenter();
                    $('#current_user_status').fadeOut().text(result['status']).fadeIn();
                } else {
                    alert('Error updating user status');
                }
            }
        });
    });

    if ($('#users_list_table').length) {
        reload_controlcenter();
    }

    $('#logout_button').on('click', function () {
        $.removeCookie('csrftoken');
        $.removeCookie('session_id');
        $(location).attr("href", $(this).attr('data-href'));
    });

    $('#username_filter').on('keyup', function () {
        reload_controlcenter($(this).val(), $('#status_filter').val());

    });

    $('#status_filter').on('change', function () {
        reload_controlcenter($('#username_filter').val(), $(this).val());

    });
});

function reload_controlcenter(username, status) {

    username = arguments[0] || '';
    status = arguments[1] || '';

    $.ajax({
        type: 'GET',
        data: {'username': username,  'status': status},
        url: $('#users_list_table').attr('data-action'),
        success: function (result) {
            if (200 == result['status_code']) {
                render_table(result['data'])
            } else {
                alert('Error loading users list');
            }
        }
    })
}

function render_table(data) {

    var users_table = $('#users_list_table');
    users_table.html('<tbody></tbody>');

    if (data.length > 0) {
        $.each(data, function (idx, row) {
            users_table.append(
                '<tr' + ('On Vacation' == row['status'] ? ' class="danger"' : '') + '><td>' + row['username'] + ' (' + row['status'] + ')' + '</td></tr>'
            );
        })
    } else {
        users_table.append('<tr class="warning"><td>No users found matching your criteria</td></tr>');
    }
}