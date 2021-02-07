$(function () {
    $("#PINform").draggable();
});

$("#PINcode").html(
    "<form name='PINform' id='PINform' autocomplete='off' draggable='true'>" +
    token +
    "<input id='PINbox' type='password' value='' name='PINbox' disabled />" +
    "<br/>" +
    "<input type='button' class='PINbutton' name='1' value='1' id='1' onClick=addNumber(this); />" +
    "<input type='button' class='PINbutton' name='2' value='2' id='2' onClick=addNumber(this); />" +
    "<input type='button' class='PINbutton' name='3' value='3' id='3' onClick=addNumber(this); />" +
    "<br>" +
    "<input type='button' class='PINbutton' name='4' value='4' id='4' onClick=addNumber(this); />" +
    "<input type='button' class='PINbutton' name='5' value='5' id='5' onClick=addNumber(this); />" +
    "<input type='button' class='PINbutton' name='6' value='6' id='6' onClick=addNumber(this); />" +
    "<br>" +
    "<input type='button' class='PINbutton' name='7' value='7' id='7' onClick=addNumber(this); />" +
    "<input type='button' class='PINbutton' name='8' value='8' id='8' onClick=addNumber(this); />" +
    "<input type='button' class='PINbutton' name='9' value='9' id='9' onClick=addNumber(this); />" +
    "<br>" +
    "<input type='button' class='PINbutton clear' name='-' value='Стереть' id='-' onClick=clearForm(this); />" +
    "<input type='button' class='PINbutton' name='0' value='0' id='0' onClick=addNumber(this); />" +
    "<input type='button' class='PINbutton enter' name='+' value='Войти' id='+' onClick=submitForm(PINbox); />" +
    "</form>"
);

function addNumber(e) {
    var v = $("#PINbox").val();
    $("#PINbox").val(v + e.value);
}

function clearForm(e) {
    if (jQuery('#PINbox').val() === "") {
        jQuery('#header').css({'opacity': '1', 'pointer-events': 'all'});
        jQuery('#body').css({'opacity': '1', 'pointer-events': 'all'});
        jQuery('#PINcode').hide('fast');

    } else {
        $("#PINbox").val("");
    }

}

function submitForm(e) {
    if (e.value == "") {
        jQuery('#PINform').effect('bounce', 'slow');
    } else {
        var form = {};
        var csrf = jQuery('input[name=csrfmiddlewaretoken]').val();
        form['csrfmiddlewaretoken'] = csrf;
        form['code'] = e.value;
        console.log(form);
        jQuery.ajax({
            url: 'http://'+jQuery(location).attr('hostname')+':8000/simpleAdmin/access/',
            method: 'POST',
            data: form,
            success:function (data) {
                if (data === 'True'){
                    window.location.replace('/simpleAdmin')
                }
                else{
                    jQuery('#PINform').effect('bounce', 'slow');
                    clearForm('');
                }
            }
        });
    }
    ;
};

function show_pin() {
    jQuery('#header').css({'opacity': '0.5', 'pointer-events': 'none'});
    jQuery('#body').css({'opacity': '0.5', 'pointer-events': 'none'});
    jQuery('#PINcode').show('fast')
}
