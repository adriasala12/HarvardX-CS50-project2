

function addRow() {

    // We only want to allow to create one channel at the time
    document.getElementById('create').disabled = true;

    const div = document.createElement('div');

    div.className = 'row';
    div.id = "x"

    document.getElementById('content').appendChild(div);

    const form = document.createElement('form');
    form.action = "addChannel";
    form.name = "yourForm";
    form.id = "theForm";
    form.method = "post";
    form.className = "col";

    document.getElementById('x').appendChild(form);

    const div2 = document.createElement('div');
    div2.className = "form-group m-5 row";
    div2.id = "div2";

    document.getElementById('theForm').appendChild(div2);

    const text = document.createElement('input');
    text.type = "text";
    text.name = "fname";
    text.id = "fname";
    text.className = "col-6 m-1 form-control form-control-lg";
    text.placeholder = "Enter a name here"

    const but = document.createElement('input');
    but.type = "submit";
    but.value = "submit";
    but.className = "m-1 btn btn-light btn-lg";

    document.getElementById('div2').appendChild(text);
    document.getElementById('div2').appendChild(but);

}

function addChannel() {

    document.getElementById('x').remove();
    document.getElementById('create').disabled = false;
}
