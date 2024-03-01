(function($) {
    $(document).ready(function() {
        $('.validar-titulo-btn').click(function() {
            var id = $(this).data('id');
            $.ajax({
                url: '/admin/pessoa/validar_titulo/',
                data: {
                    id: id
                },
                dataType: 'json',
                success: function(data) {
                    alert('Local de votação validado com sucesso!'); // Mensagem opcional de confirmação
                }
            });
        });
    });
})(django.jQuery);
