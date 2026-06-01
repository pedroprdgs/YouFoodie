document.addEventListener("DOMContentLoaded",  () => {
    const filtros = document.querySelectorAll(".category-filter");
    const pratos = document.querySelectorAll(".prato-item");
    const busca = document.getElementById("search-pratos");

    let categoriaAtual = "Todos";

    function filtrar(){
        const texto = busca.value.toLowerCase();

        pratos.forEach(prato => {
            const categoria = prato.dataset.category;
            const nome = prato.dataset.name;

            const categoriaValida = categoriaAtual === "Todos" || categoria === categoriaAtual;

            const textoValido = nome.includes(texto)

            prato.style.display = categoriaValida && textoValido ? "" : "none";
        });
    }
    filtros.forEach(botao => {
        botao.addEventListener("click", () => {
            filtros.forEach(btn => {
                btn.classList.remove("btn-foodie-large");
                btn.classList.add("btn-outline-foodie");
            });
            botao.classList.remove("btn-outline-foodie");
            botao.classList.add("btn-foodie-large");

            categoriaAtual = botao.dataset.category;

            filtrar();
        });
    });
    busca.addEventListener("input", filtrar);
});