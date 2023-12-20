let obj_to_tr = (obj) => {
    return `<tr>
        <td>${obj["#"]}</td>
        <td>${obj.Model}</td>
        <td>${obj.Creator}</td>
        <td>${obj.Access}</td>
        <td>${obj["Submission Date"]}</td>
        <td>${obj["Network Security"]}</td>
        <td>${obj.Vulnerability}</td>
        <td>${obj["Memory Safety"]}</td>
        <td>${obj["Web Security"]}</td>
        <td>${obj["Application Security"]}</td>
        <td>${obj.Cryptography}</td>
        <td>${obj["System Security"]}</td>
        <td>${obj["Software Security"]}</td>
        <td>${obj["PenTest"]}</td>
        <td>${obj.Overall}</td>
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