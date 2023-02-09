const ul = document.getElementById("publications");
const url = "/api/articles/event_get_publications"

function publicationLine(article){
    let li = document.createElement('li');
    let span = document.createElement('span');
    span.innerHTML = `${article.title} ${article.published}`;
    li.appendChild(span)
    ul.appendChild(li)
}

fetch(url)
    .then(response => response.json())
    .then(data => data["articles"].map(article => publicationLine(article)));
