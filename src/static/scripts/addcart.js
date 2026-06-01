document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.add-cart').forEach(btn => {
        btn.addEventListener('click', async() => {
            const pratoId = btn.dataset.prato;

            try{
                await fetch('/carrinho/adicionar', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ id_prato: pratoId })
                });
            } catch (error) {
                console.error('Erro ao adicionar produto:', error);
            }
        });
    });
});