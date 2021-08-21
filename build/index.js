let tutorials = |;
let nav = document.getElementById("nav");

if (nav != undefined){
    for (let i=0;i<tutorials.length;i++){
        let name = tutorials[i];
        
        let displayName = "";
        for (let j=0;j<name.split("-").length;j++){
            let part = name.split("-")[j];
            displayName += part.charAt(0).toUpperCase() + part.slice(1) + " "
        }
    
        nav.innerHTML += '<a href="' + name + `" class="post">` + i + ". " + displayName + '</a>'
    }    
}

function getTutorials(){
    return tutorials;
}