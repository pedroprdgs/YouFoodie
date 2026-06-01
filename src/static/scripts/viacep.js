document.addEventListener("DOMContentLoaded", () => {
    const cepInput = document.getElementById("cep");

    if(!cepInput) return;

    let ultimoCep = '';

    cepInput.addEventListener("input", async () => {
        const cep = cepInput.value.replace(/\D/g, '');

        if(cep.length !== 8 || ultimoCep == cep) return;

        ultimoCep = cep;

        try{
            const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
            const data = await response.json();

            if(data.erro) return;

            preencherCampo('estado', data.uf);
            preencherCampo('cidade', data.localidade);
            preencherCampo('rua', data.logradouro);
        } catch(error){
            console.error(error);
        }
    });

    function preencherCampo(id, valor){
        const campo = document.getElementById(id);

        if(!campo) return;

        campo.value = valor;
        campo.dispatchEvent(new Event('input', {
            bubbles: true
        }));
    }
});