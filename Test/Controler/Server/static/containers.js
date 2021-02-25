var primary='#2F3542'
var secondary='#0984e3'
var accent='#E3F2FD'
var dark='black'
function show(show,hide1,hide2){
    document.getElementById(show).style.display="block";
    document.getElementById(hide1).style.display="none"
    document.getElementById(hide2).style.display="none"
}
function active(element){
    document.getElementById(element).style.background=dark;
    document.getElementById(element).style.color=accent;
}
function deactivate(element){
    document.getElementById(element).style.background=primary;
    document.getElementById(element).style.color=accent;
}