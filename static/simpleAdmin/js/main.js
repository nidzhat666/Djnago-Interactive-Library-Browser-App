function pin_remove(e) {
    var val = jQuery(e).attr('id');

    jQuery.ajax({
        url: 'http://' + jQuery(location).attr('hostname') + ':8000/simpleAdmin/pinRemove',
        method: 'GET',
        data: {'element': val},
        success: function (data) {
            if (data === 'Low') {
                alert('Что бы удалить пароль нужно иметь не меньше одного')
            }
            if (data === 'success') {
                jQuery(e).parent().remove()
            }
            console.log(data)
        }

    })
}

function closeTab(i) {
    window.open('http://' + jQuery(location).attr('hostname') + ':8000/simpleAdmin/', '_self', '');
    window.close();
}

function voiskaDelete(i) {
    var a = jQuery('.name' + i).text();
    var conf = confirm('Уверены что хотите удалить элемент?' + a);
    if (conf === true) {
        var data = {'i': i};
        jQuery.ajax({
            url: 'http://' + jQuery(location).attr('hostname') + ':8000/simpleAdmin/voiskaDelete',
            method: 'GET',
            data: data,
            success: function (dat) {
                if (dat === 'Success') {
                    jQuery('.tr' + i).hide('slow', function () {
                        jQuery(this).remove();
                    });
                }
            }
        })
    }

}

jQuery(document).ready(function () {
    jQuery('.formAdd').draggable()
});

function showAddWindow() {
    jQuery('.container').css('opacity', '0.3');
    jQuery('.formAdd').show('slow');
}

function hideAddWindow() {
    jQuery('.container').css('opacity', '1');
    jQuery('.formAdd').hide('slow');
    jQuery('input[name$="name"]').val('');
}

function formAddSend(i) {
    var ser_data = jQuery(i).serialize();
    jQuery.ajax({
        url: 'http://' + jQuery(location).attr('hostname') + ':8000/simpleAdmin/voiskaAdd/',
        method: 'POST',
        data: ser_data,
        success: function (data) {
            appendVoiska(data)
        }
    })
}

function appendVoiska(data) {
    var $doc = $('<tr style="display: none" class="tr' + data['id'] + '">\n' +
        '                    <td>\n' +
        data['id'] +
        '                    </td>\n' +
        '                    <td class="name{{ foo.id }}">\n' +
        data['name'] +
        '                    </td>\n' +
        '                    <td>\n' +
        '                        <button class="btn btn-danger" onclick="voiskaDelete(' + data['id'] + ')">Удалить</button>\n' +
        '                    </td>\n' +
        '                </tr>');
    jQuery('.table > tbody').append($doc);
    hideAddWindow();
    jQuery('.tr' + data['id']).show('slow')
}

function reset() {
    jQuery('input').val("");
    jQuery('.authorAddForm img').hide();
    jQuery('.authorAddForm input[required]').removeAttr('style');
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        console.log(input.files[0]['name']);
        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result).show();
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function authorAddSubmit() {
    var number = 0;
    jQuery('.authorAddForm input[required]').each(function (i) {
        if (jQuery(this).val() === "") {
            number++;
            jQuery(this).css('border', '2px solid red')
        }
    });
    if (number === 0) {
        jQuery('.authorAddForm').submit();
    }
}

function voiskaAdd(){
    jQuery('.voiskaAdd').submit();
    jQuery('.voiskaAdd input').val("")
}