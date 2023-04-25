document.addEventListener('DOMContentLoaded', function() {
  const buttons = document.querySelectorAll('.button-master');
  buttons.forEach(function(button) {
    button.addEventListener('click', function() {
      const master_id = this.closest('.image').getAttribute('data-master-id');
      window.location.href = '/portfolio/master' + master_id + '/';
    });
  });
});