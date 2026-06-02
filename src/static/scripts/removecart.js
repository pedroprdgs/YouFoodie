document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.remove-cart').forEach(btn => {
        btn.addEventListener('click', async() => {
            const pratoId = btn.dataset.prato;

            try{
                const response = await fetch('/carrinho/remover', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ id_prato: pratoId })
                });
                const removido = await response.json();
                showToast(removido.message, removido.success ? 'success' : 'warning');
            } catch (error) {
                console.error('Erro ao remover produto:', error);
                showToast('Erro ao remover produto.', 'danger');
            }
        });
    });
});