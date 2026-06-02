document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.clear-cart-btn').forEach(btn => {
        btn.addEventListener('click', async() => {
            if(confirm('Deseja mesmo limpar seu carrinho?')){
                try{
                    await fetch('/carrinho/limpar', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' }
                    });
                    showToast('Carrinho limpo com sucesso!');
                    setTimeout(() => {
                        location.reload();
                    }, 1500);
                } catch (error) {
                    console.error('Erro ao limpar carrinho:', error);
                    showToast('Erro ao limpar carrinho.', 'danger');
                }
            }
        });
    });
});