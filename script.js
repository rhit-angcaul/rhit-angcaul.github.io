
window.addEventListener("DOMContentLoaded", domLoaded);


function domLoaded(){
    let resumeBtn = document.querySelector('[name="resumeBtn"]')
    let portBtn = document.querySelector('[name="portBtn"]')
    let handBtn = document.querySelector('[name="handBtn"]')
    let linkBtn = document.querySelector('[name="linkBtn"]')


// https://stackoverflow.com/questions/16562577/how-can-i-make-a-button-redirect-my-page-to-another-page

    resumeBtn.addEventListener("click", function(){
    window.location.href="https://rhit-angcaul.github.io/resume.html"
    })

    portBtn.addEventListener("click", function(){
    window.location.href="https://rhit-angcaul.github.io/portfolio.html"
    })
    handBtn.addEventListener("click", function(){
    window.location.href="https://app.joinhandshake.com/profiles/caulfias"
    })
    linkBtn.addEventListener("click", function(){
    window.location.href="https://www.linkedin.com/in/angela-caulfield-a092073aa/"
    })
}
