

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('theForm').onsubmit = () => {

        // // Show empty string alert
        // var name = document.getElementById('fname').value;
        // if (name == null) {
        //     alert(`The name cannot be an empty string`);
        // }
        //
        // var success = '{{ success }}';
        // console.log(success);
        // if (success == "False") {
        //     alert(`This name is already in use`);
        // }

    };
});

// document.addEventListener('DOMContentLoaded', () => {
//     document.querySelector("#theForm").onsubmit = () => {
//         const request = new XMLHttpRequest();
//         request.open('POST', '/addChannel')
//
//         request.onload() = () => {
//             if request.responseText != null {
//                 alert("This name is already in use.")
//             }
//         }
//
//         request.send();
//         return false;
//     };
// });

function addRow() {

    // We only want to allow to create one channel at the time
    document.getElementById('create').disabled = true;

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
    console.log("hello");
    document.getElementById('theForm').remove();
    document.getElementById('create').disabled = false;
}
