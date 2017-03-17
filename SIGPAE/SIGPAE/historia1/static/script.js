$( document ).ready(function() {
  var $label = $("<label>").text('Período de Entrada en Vigencia');
  //$('#id_year').prepend($label)
  $($label).insertBefore('#id_year');
  $($label).insertBefore('#id_fecha_vigano');

  $('select[name=guardar]').on('change', function() {
      if ($(this).val() === 'PASA') {
        $("#msg").show();
      } else {
        $("#msg").hide();      
      }
  });
});
