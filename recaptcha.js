//
// <script type="text/javascript">
//   var onloadCallback = function() {
//     $(".g-recaptcha").each(function() {
//       var el = $(this);
//       grecaptcha.render($(el).attr("id"), {
//         "sitekey": "6Ldkf5cUAAAAAJYIJSB5l-akAN_efBssFaMJLQNe",
//         "callback" : function(token) {
//           $(el).parent().find("g-recaptcha-response").val(token);
//           $(el).parent().submit();
//         }
//       })
//     })
//   }
<script>
var on_code_form_submit = function(e) {
  var response = grecaptcha.getResponse();
  if (!response) {
    e.preventDefault();
    $(this).attr('data-submit-please', 'true')
    grecaptcha.execute();
  } else {
    $(this).find('input[name="recaptcha"]').val(response)
  }
};

function recaptcha_submit(token) {
  var $form = $('form[data-submit-please="true"]');
  $form.find('input[name="recaptcha"]').val(token)
  $form.submit();
}
</script>
