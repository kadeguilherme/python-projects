function add_carro() {
    container = document.getElementById('form-carro')

    html = "<br>  <div class='row'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro' > </div><div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='placa' > </div> </div>"

    container.innerHTML += html
}

function exibir_form(tipo) {
    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att_cliente')

    if (tipo == "1") {
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"

    } else if (tipo == "2") {
        add_cliente.style.display = "none";
        att_cliente.style.display = "block"
    }
}


function dados_cliente() {
    cliente = document.getElementById('cliente-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_cliente = cliente.value

    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function (result) {
        return result.json()
    }).then(function (data) {
        document.getElementById('form-att-cliente').style.display = 'block'

        nome = document.getElementById('nome')
        nome.value = data['cliente']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['cliente']['sobrenome']

        cpf = document.getElementById('cpf')
        cpf.value = data['cliente']['cpf']

        email = document.getElementById('email')
        email.value = data['cliente']['email']

        div_carros = document.getElementById('carros')

        for (i = 0; i < data['carros'].length; i++) {
            console.log(data['carros'][i]['fields']['carro'])
            console.log(data['carros'][i])
            div_carros.innerHTML += "\<form action='/clientes/update_carro/" + data['carros'][i]['id'] + "' method='POST'>\
                <div class='row'>\
                        <div class='col-md'>\
                            <input class='form-control' name='carro' type='text' value='" + data['carros'][i]['fields']['carro'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' name='placa' type='text' value='" + data['carros'][i]['fields']['placa'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='btn btn-lg btn-success' type='submit'>\
                        </div>\
                    </form>\
                    <div class='col-md'>\
                        <a href='/clientes/excluir_carro/"+ data['carros'][i]['id'] + "' class='btn btn-lg btn-danger'>EXCLUIR</a>\
                    </div>\
                </div><br>"
        }
    })

}