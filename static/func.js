
function imagem1(){
document.getElementById('id').src="static/alunos1.png";
setTimeout("imagem2()", 2000)
document.getElementById('aId').href="link1.html"
}

function imagem2(){
document.getElementById('id').src="static/alunos2.png";
setTimeout("imagem3()", 2000)
document.getElementById('aId').href="link2.html"
}

function imagem3(){
document.getElementById('id').src="static/alunos3.png";
setTimeout("imagem1()", 2000)
document.getElementById('aId').href="link3.html"
}