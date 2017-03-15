$( document ).ready(function() {
  var $label = $("<label>").text('Período de Entrada en Vigencia');
  //$('#id_year').prepend($label)
  $($label).insertBefore('#id_year');
  $($label).insertBefore('#id_fecha_vigano');

  var $alert = '<div class="alert alert-warning"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>TEST</div>'; 
  $('#id_guardar').change(function() {
      if ($(this).val() === 'PASA') {
          //$($alert).insertAfter('#id_guardar');
          $('#id_guardar').append($alert);
      }
  });
});