$( document ).ready(function() {
  var $label = $("<label>").text('Período de Entrada en Vigencia');
  var $text = $("<i>").text('dd/mm/aaaa');
  //$('#id_year').prepend($label)
  $($label).insertBefore('#id_year');
  $($label).insertBefore('#id_fecha_vigano');
  $('<i name="test" hidden>dd/mm/aaaa</i>').insertAfter('label[for=id_fecha]');

  $('select[name=guardar]').on('change', function() {
      if ($(this).val() === 'PASA') {
        $("#msg").show();
      } else {
        $("#msg").hide();      
      }
  });
});
