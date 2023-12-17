let obj_to_tr = (obj) => {
    return `<tr>
        <td>${obj["#"]}</td>
        <td>${obj.Model}</td>
        <td>${obj.Creator}</td>
        <td>${obj.Access}</td>
        <td>${obj["Submission Date"]}</td>
        <td>${obj.Avg}</td>
        <td>${obj["Network Security"]}</td>
        <td>${obj.Vulnerability}</td>
        <td>${obj["Memeory Security"]}</td>
        <td>${obj["Web Security"]}</td>
        <td>${obj["App Securiry"]}</td>
        <td>${obj.Cryptography}</td>
        <td>${obj["System Security"]}</td>
        <td>${obj.Pentest}</td>
    </tr>`
}

let table = document.getElementById("results");
html = "";
for (let i of leaderboard) {
    html += obj_to_tr(i);
}
table.getElementsByTagName("tbody")[0].innerHTML = html;
function reflow(elt){
    console.log(elt.offsetHeight);
}
reflow(table);