let obj_to_tr = (obj) => {
    return `<tr>
        <td>${obj["#"]}</td>
        <td style="text-align: left;"><strong>${obj.Method}</strong></td>
        <td><a href="${obj.Source.Link}" class="ext-link" style="font-size: 16px;">${obj.Source.Source}</a></td>
        <td>${obj.Date}</td>
        <td>${obj["#Size"]}</td>
        <td>${obj["#Param"]}</td>
        <td>${obj.Avg}</td>
        <td>${obj.NAT}</td>
        <td>${obj.SOC}</td>
        <td>${obj.LAN}</td>
        <td>${obj.TXT}</td>
        <td>${obj.IMG}</td>
        <td>${obj.NO}</td>
        <td>${obj["G1-6"]}</td>
        <td>${obj["G7-12"]}</td>
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