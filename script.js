
let resumeBtn = document.getElementsByName("resumeBtn")
let portBtn = document.getElementsByName("portBtn")
let handBtn = document.getElementsByName("handBtn")
let linkBtn = document.getElementsByName("linkBtn")


// https://stackoverflow.com/questions/16562577/how-can-i-make-a-button-redirect-my-page-to-another-page

resumeBtn.onClick = function(){
    location.href="/resume.html"
}
