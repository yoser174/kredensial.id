const spinnerWrapperEl = document.querySelector('.spinner-wrapper');

window.addEventListener('load',()=>{
  spinnerWrapperEl.style.opacity = 0;

  setTimeout(()=>{
    spinnerWrapperEl.style.display = 'none';
  },200);

});

document.addEventListener('DOMContentLoaded', function () {
  const forms = document.querySelectorAll('.needs-validation');

  forms.forEach(function (form) {
      form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
              event.preventDefault();
              event.stopPropagation();
              form.classList.add('was-validated');
          }
      }, false);
  });

  document.body.addEventListener('htmx:configRequest', function (event) {
      const form = event.target.closest('form');
      if (form && !form.checkValidity()) {
          event.preventDefault();
          form.classList.add('was-validated');
      }
  });
});
