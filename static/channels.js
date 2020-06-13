

function addRow() {

    // We only want to allow to create one channel at the time
    document.getElementById('create').disabled = true;

    const div = document.createElement('div');

    div.className = 'row';
    div.id = "x"

    div.innerHTML = `
        <!-- <form class="col" action="{{ url_for('addChannel')}}" method="post" style="background-color:blue">
            <div class="form-group m-5 row">
                <input name="txt" id="txt" class="col-6 m-1 form-control form-control-lg" type="text" placeholder="Enter your name here" autocomplete="false">
                <button id="submit" class="m-1 btn btn-light btn-lg" onclick="addChannel()">Add</button>
            </div>
        </form> -->



    `;

    document.getElementById('content').appendChild(div);

    const form = document.createElement('form');
    form.action = "addChannel";
    form.name = "yourForm";
    form.id = "theForm";
    form.method = "post";

    document.getElementById('x').appendChild(form);

    const text = document.createElement('input');
    text.type = "text";
    text.name = "fname";
    text.id = "fname";

    const but = document.createElement('input');
    but.type = "submit";
    but.value = "submit";

    document.getElementById('theForm').appendChild(text);
    document.getElementById('theForm').appendChild(but);

}

function addChannel() {

    document.getElementById('x').remove();
    document.getElementById('create').disabled = false;
}
