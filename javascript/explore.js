let topics = [
    'All',
    'SoftwareSecurity',
    'NetworkSecurity',
    'Vulnerability',
    'MemorySafety',
    'WebSecurity',
    'AppSecurity',
    'Cryptography',
    'SystemSecurity',
    'PenTest'
]



let topic_dd = make_dropdown("Choose a topic:", topics, "topic-dd");
let optbtn = document.getElementsByClassName("optionsbtn")[0];
let closebtn = document.getElementsByClassName("closebtn")[0];
let optionpanel = document.getElementById("option-panel");
let body = document.getElementById("content-body");
let display = document.getElementById("display");
let optboxes = document.getElementsByClassName("optbox");
let opt_dds = document.getElementsByClassName("opt-dd");
let filter_submit = document.getElementById("filter-submit");

optboxes[0].innerHTML += topic_dd;

topic_dd = document.getElementById("topic-dd");


let filters = {};

optbtn.addEventListener("click", openNav);
closebtn.addEventListener("click", closeNav);


for (each of opt_dds) {
    each.addEventListener("change", change_filters);
}
filter_submit.addEventListener("click", filter_data);

filter_data();

function openNav() {
    optionpanel.style.width = "20vw";
    display.style.width = "60vw";
    for (each of optionpanel.children) {
        each.style.display = "block";
    }
}

function closeNav() {
    optionpanel.style.width = "0";
    display.style.width = "80vw";
    for (each of optionpanel.children) {
        each.style.display = "none";
    }
}


function change_filters(e) {
    filters.topic = document.getElementById("topic-dd").value;
}

function create_page(d) {
    if (d.length === 0) {
        body.innerHTML = "<p>No example satisfies All the filters.</p>";
    } else {
        col1 = create_col(d.slice(0, d.length / 2));
        col2 = create_col(d.slice(d.length / 2));
        body.innerHTML = col1 + col2;
    }
    reflow(body);
    console.log("reflowed");
}

function create_col(data) {
    res = [];
    for (each of data) {
        res.push(create_example(each));
    }
    return `<div class="display-col"> ${res.join("")} </div>`;
}


function create_example(data) {
    let question = make_qt(data.question);
    let choices = make_choices(data.choices);
    let answer = make_answer(data.answer);
    html = make_box([question, choices, answer]) + "<hr/>";
    return html;
}


function convert_latex(data) {
    const re = /(\$+)([^\$]*?[^\\])\1|\\begin\{tabular\}.*?\\end\{tabular\}/gs;
    let html = '';

    let match;
    let lastIndex = 0;
    while ((match = re.exec(data)) !== null) {
        html += `<span>${data.slice(lastIndex, match.index)}</span>`;

        if (match[0].startsWith('\\begin{tabular}')) {
            const table = match[0];
            const tableHtml = '...'; 
            html += tableHtml;
        } else {
            const latex = match[2];
            const formula = katex.renderToString(latex, {throwOnError: false});
            html += `<span>${formula}</span>`;
        }

        lastIndex = match.index + match[0].length;
    }

    html += `<span>${data.slice(lastIndex)}</span>`;

    return html;
}

function make_qt(text) {
    text = text.replace(/^\n+|\n+$/g, '');
    let html = `
            <p><b>Question </b></p>
            <p class="question-txt">${convert_latex(text).replace(/\\n|\n/g, "<br>")}</p>
    `;
    return html;
}

function make_box(contents, cls = "") {
    if (contents.join("").length === 0) return "";
    let html = `
        <div class="box ${cls}"> 
            ${contents.join(" ").replace(/\\n|\n/g, "<br>")}
        </div>
    `;
    return html;
}

function make_choices(choices) {
    let temp = "";
    let len = 0;
    for (each of choices) {
        let html = make_choice(each);
        temp += html;
        len += each.length;
    }
    let html = "";
    if (len < 60)
        html = `<p><b>Choices </b></p><div class="choices">${convert_latex(temp).replace(/\\n|\n/g, "<br>")}</div>`;
    else
        html = `<p><b>Choices </b></p><div class="choices-vertical">${convert_latex(temp).replace(/\\n|\n/g, "<br>")}</div>`;
    return html;
}

function make_choice(choice) {
    let html = `<div class="choice-txt">${convert_latex(choice).replace(/\\n|\n/g, "<br>")}</div>`;
    return html;
}

function make_answer(answer) {
    let html = `<p><b>Answer </b></p><p class="answer-txt">${convert_latex(answer)}</p>`;
    return html;
}

function make_dropdown(label, options, id, default_ind = 0) {
    let html = "";
    for (let i = 0; i < options.length; i++) {
        if (i === default_ind)
            html += `<option value="${options[i]}" selected> ${options[i]} </option>`;
        else
            html += `<option value="${options[i]}"> ${options[i]} </option>`;
    }
    html = `<label class="dd-label">${label} <select id="${id}" class="opt-dd"> ${html} </select> </label><br/>`;
    return html;
}

function filter_data() {
    change_filters();
    res = problem_data;
    if (filters.topic !== "All")
        res = res.filter(e => e.topics.includes(filters.topic));
    d = _.sample(res, Math.min(100, res.length));
    create_page(d);
}

function reflow(elt) {
    elt.offsetHeight;
}
