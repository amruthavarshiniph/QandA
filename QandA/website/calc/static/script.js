var counter = 0;

var settingsMenu = document.querySelector(".settings-menu");

function likebtn() {
    counter++;
    document.getElementById("votes").innerHTML = counter;
}

function dislikebtn() {
    counter--;
    document.getElementById("votes_1").innerHTML = counter;
}

function settingsMenuToggle(){
    settingsMenu.classList.toggle("settings-menu-height");
}


// function comment_fun(){
//     var data = document.getElementById("ques").value;
//     // console.log(data);
//     alert(data);
// }