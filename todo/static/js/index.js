

let containerStyle = document.getElementById("container").style;
let temp
function open_form() {
    document.getElementById("new_task").style.display = "block";
    document.getElementById("completed").style.display = "none";
    containerStyle.opacity = "0.5";
}
function close_form() {
    document.getElementById("new_task").style.display = "none";
    containerStyle.opacity = "1";
}
function open_complete(id) {
    document.getElementById("completed").style.display = "block";
    document.getElementById("new_task").style.display = "none";
    containerStyle.opacity = "0.5";
    document.getElementById("task_id").value=id;
}
function close_complete() {
    document.getElementById("completed").style.display = "none";
    containerStyle.opacity = "1"
}