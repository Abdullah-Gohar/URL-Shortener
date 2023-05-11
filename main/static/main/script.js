
function copyDivToClipboard() {
        // Get the text field
        var copyText = document.getElementById("shortened-url").innerText;
        navigator.clipboard.writeText(copyText);

        // Alert the copied text
        alert("Copied the text: " + copyText);
} 

function scrollToSection(id){
        const section = document.getElementById(id);
        section.scrollIntoView({behavior: "smooth"});
}