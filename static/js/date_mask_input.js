document.addEventListener('DOMContentLoaded', function() {
    var dateField = document.querySelector('input[data-mask="date"]');
    if (dateField) {
        $(dateField).inputmask("99/99/9999", { "placeholder": "dd/mm/yyyy" });
    }
});
